from fastapi import FastAPI, Request, Response
import httpx
import re

app = FastAPI()
TARGET_URL = "https://frsim.com"

@app.api_route("/proxy/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def reverse_proxy(request: Request, path: str):
    url = f"{TARGET_URL}/{path}"
    if request.query_params:
        url += f"?{request.query_params}"

    # Forward headers (excluding Host so target accepts the request)
    headers = dict(request.headers)
    headers.pop("host", None)

    async with httpx.AsyncClient(follow_redirects=True) as client:
        resp = await client.request(
            method=request.method,
            url=url,
            headers=headers,
            content=await request.body(),
            cookies=request.cookies
        )

    # Strip headers that block embedding or cause mismatch errors
    excluded_headers = {"content-encoding", "content-length", "transfer-encoding", "connection", "x-frame-options", "content-security-policy"}
    response_headers = {k: v for k, v in resp.headers.items() if k.lower() not in excluded_headers}

    content = resp.content
    content_type = resp.headers.get("content-type", "")

    # Rewrite relative asset/API links in HTML so they route through /proxy/
    if "text/html" in content_type:
        html = resp.text
        html = re.sub(r'(href|src|action)="/', r'\1="/proxy/', html)
        content = html.encode("utf-8")

    return Response(content=content, status_code=resp.status_code, headers=response_headers)