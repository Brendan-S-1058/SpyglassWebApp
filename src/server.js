const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const path = require("path");
const zlib = require("zlib");
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

const TARGET_SIM = 'https://rebuilt.frsim.com';
const TARGET_WS = 'https://reefscape-ws.frsim.com';

// 1. Proxy for the FRSim Accounts & Multiplayer Backend
app.use('/ws-proxy', createProxyMiddleware({
  target: TARGET_WS,
  changeOrigin: true,
  ws: true,
  pathRewrite: {
    '^/ws-proxy': '',
  },
  on: {
    proxyReq: (proxyReq) => {
      // Spoof Origin/Referer so FRSim's backend accepts the connection
      proxyReq.setHeader('Origin', TARGET_SIM);
      proxyReq.setHeader('Referer', `${TARGET_SIM}/`);
    },
    proxyRes: (proxyRes) => {
      delete proxyRes.headers['x-frame-options'];
      delete proxyRes.headers['content-security-policy'];
    },
  },
}));

// 2. Proxy for the FRSim Frontend + Rewriting the hardcoded backend URL inside JS files
const simProxyOptions = {
  target: TARGET_SIM,
  changeOrigin: true,
  ws: true,
  selfHandleResponse: true, // Lets us swap out the hardcoded reefscape-ws URL in JS bundles
  on: {
    proxyRes: (proxyRes, req, res) => {
      delete proxyRes.headers['x-frame-options'];
      delete proxyRes.headers['content-security-policy'];
      delete proxyRes.headers['content-length'];

      const contentType = proxyRes.headers['content-type'] || '';
      const encoding = proxyRes.headers['content-encoding'];
      const isRewriteable = contentType.includes('javascript') || contentType.includes('text/html');

      // Pass images, fonts, wasm, and binary files straight through untouched
      if (!isRewriteable) {
        res.writeHead(proxyRes.statusCode, proxyRes.headers);
        proxyRes.pipe(res);
        return;
      }

      // Buffer and decompress JS/HTML to replace the hardcoded backend URL
      const chunks = [];
      proxyRes.on('data', (chunk) => chunks.push(chunk));
      proxyRes.on('end', () => {
        let buffer = Buffer.concat(chunks);

        const decompress = (buf, cb) => {
          if (encoding === 'gzip') zlib.gunzip(buf, cb);
          else if (encoding === 'br') zlib.brotliDecompress(buf, cb);
          else if (encoding === 'deflate') zlib.inflate(buf, cb);
          else cb(null, buf);
        };

        decompress(buffer, (err, decoded) => {
          if (err) {
            res.writeHead(proxyRes.statusCode, proxyRes.headers);
            res.end(buffer);
            return;
          }

          delete proxyRes.headers['content-encoding'];
          let body = decoded.toString('utf8');

          // Point all account & multiplayer calls to your own /ws-proxy route
          const myOrigin = `https://${req.headers.host}/ws-proxy`;
          const myWsOrigin = `wss://${req.headers.host}/ws-proxy`;
          body = body
            .replaceAll('https://reefscape-ws.frsim.com', myOrigin)
            .replaceAll('wss://reefscape-ws.frsim.com', myWsOrigin);

          res.writeHead(proxyRes.statusCode, proxyRes.headers);
          res.end(body);
        });
      });
    },
  },
};

const simAssetPrefixes = [
  '/_next',
  '/assets',
  '/models',
  '/textures',
  '/wasm',
  '/manifest.webmanifest',
  '/favicon.ico',
  '/socket.io',
];

app.use(createProxyMiddleware({
  ...simProxyOptions,
  pathFilter: (pathname) => simAssetPrefixes.some((prefix) => pathname.startsWith(prefix)),
}));

app.use('/proxy', createProxyMiddleware({
  ...simProxyOptions,
  pathRewrite: {
    '^/proxy': '',
  },
}));

app.use(express.json({limit: '10mb'}));
app.use(cors()); // Enables CORS for frontend requests

const PORT = process.env.PORT || 10000; // Use Render's assigned port or default to 10000

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server running on port ${PORT}`);
});


const { execSync } = require("child_process");
const { json } = require("stream/consumers");

try {
    console.log("Setting up Python environment...");
    const venvPath = path.join(__dirname, "venv");

    // Create virtual environment if it doesn't exist
    execSync(`python3 -m venv ${venvPath}`, { stdio: "inherit" });

    // Install dependencies in the virtual environment
    execSync(`${venvPath}/bin/pip install -r requirements.txt`, { stdio: "inherit" });

    console.log("Python dependencies installed successfully!");
} catch (error) {
    console.error("Failed to set up Python:", error);
}

//Api route pointing to nothing (right now)
app.post("/individual", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["Search.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/importPitFiles", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["importPitFiles.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/fullOneMatchPred", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["fullMatchPred.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/makeTeamDirs", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["makeDirs.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/teamPullMatches", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["teammatches.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/OPRgraph", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["oprPicklist.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/dprsort", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["dpr.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/oprsort", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["opr.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            console.log(jsonResponse);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    

});

app.post("/grapher", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["Grapher.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/oneMinute", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["pyStall.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/PLSort", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["pickList.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
        console.log("output to server: " + output)
        console.log("data: " + data)
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/PLSort2", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["pickList2.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
        console.log("output to server: " + output)
        console.log("data: " + data)
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/publicStorage", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["writePublic.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/failFix", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["makeAndWrite.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/matchPredinput", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["predictManual.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/EventPred", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["pullMatches.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/FindPassword", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["checkPass.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/setPassword", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["newPass.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/overall", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["Search2.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/getScoutedTeams", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["scoutedTeamList.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/logCompResults", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["storeCompRes.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/qualPL", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["magicPickList.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});

app.post("/pitScoutFiles", (req, res) => {
    const input = String(req.body);
    const venvPath = path.join(__dirname, "venv/bin/python");
    const individualProcess = spawn(venvPath, ["pitFiles.py"]);

    let output = "";

    individualProcess.stdin.write(JSON.stringify(input));
    individualProcess.stdin.end();

    individualProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    individualProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    individualProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});


// API route to execute Python script
app.post("/run-python", (req, res) => {
    const input = String(req.body); // Convert input data to JSON string
    const venvPath = path.join(__dirname, "venv/bin/python");
    const pythonProcess = spawn(venvPath, ["ScoutSheet.py"]);

    let output = "";

    // Send input to Python script
    pythonProcess.stdin.write(input);
    pythonProcess.stdin.end();

    // Capture Python script output
    pythonProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    // Handle process completion
    pythonProcess.on("close", (code) => {
        try {
            const jsonResponse = JSON.parse(output);
            res.json(jsonResponse);
        } catch (error) {
            res.status(500).json({ error: "Invalid response from Python script" });
        }
    });

    // Handle errors
    pythonProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    
});
// Serve static files from the "public" folder
app.use(express.static(path.join(__dirname, "public")));

// Catch-all route for SPA (if using React/Vue/Angular frontend)
app.get("*", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});