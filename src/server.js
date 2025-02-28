const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
app.use(express.json());
app.use(cors()); // Enables CORS for frontend requests

// API route to execute Python script
app.post("/run-python", (req, res) => {
    const input = String(req.body); // Convert input data to JSON string
    const pythonProcess = spawn("python3", ["src/ScoutSheet.py"]); // Use "python3" if needed

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

// Start the server (Only call app.listen ONCE!)
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
