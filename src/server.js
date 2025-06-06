const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
app.use(express.json());
app.use(cors()); // Enables CORS for frontend requests

const PORT = process.env.PORT || 10000; // Use Render's assigned port or default to 10000

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server running on port ${PORT}`);
});


const { execSync } = require("child_process");

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