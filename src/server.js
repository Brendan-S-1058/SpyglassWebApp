const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
app.use(express.json());
app.use(cors()); // Enables CORS for frontend requests

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

    pythonProcess.stdout.on("data", (data) => {
        console.log("Python stdout:", data.toString());
        output += data.toString();
    });
    
});

// Serve static files from the "public" folder
app.use(express.static(path.join(__dirname, "public")));

// Catch-all route for SPA (if using React/Vue/Angular frontend)
app.get("*", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Start the server (Only call app.listen ONCE!)
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
