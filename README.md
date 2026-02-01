Global Weather Reporter 🌦️
A real-time weather intelligence tool for AI agents.

Overview
The Global Weather Reporter is a simple, no-auth MCP tool that gives your AI assistant "eyes" on the world's weather. It fetches live data using the Open-Meteo API, allowing your AI to report current conditions, temperature, and wind speed for any city on Earth without needing complex API keys or login systems.

Deployment Status: ✅ Ready for Render

Key Features
🌍 Real-Time Data: Fetches live weather conditions instantly (get_weather).

📍 Smart Geocoding: Automatically converts city names (e.g., "Paris") into coordinates.

⚡ No Auth Required: Uses public, open-source APIs for zero-friction setup.

☁️ Cloud-Hosted: Persistent availability via secure SSE connection.

🚀 How to Connect (For Users)
Since this tool is hosted remotely, you need a small local "bridge" script to connect it to Claude Desktop.

Prerequisites
Python 3.10 or higher installed.

Claude Desktop installed.

Step 1: Get the Connection Script
Save the code below as client_remote.py on your computer (or clone this repo):

Python
from fastmcp.server import create_proxy

# The URL of your deployed Weather Tool
# Replace <YOUR-APP-NAME> with the actual URL provided by Render
RENDER_SSE_URL = "https://<YOUR-APP-NAME>.onrender.com/sse" 

# Initialize the proxy
mcp = create_proxy(RENDER_SSE_URL, name="Global Weather Reporter")

if __name__ == "__main__":
    mcp.run()
Step 2: Configure Claude Desktop
Open your Claude Desktop config file:

Windows: %APPDATA%\Claude\claude_desktop_config.json

Mac: ~/Library/Application Support/Claude/claude_desktop_config.json

Add this configuration:

JSON
{
  "mcpServers": {
    "weather-remote": {
      "command": "python",
      "args": ["C:\\path\\to\\your\\client_remote.py"]
    }
  }
}
(Make sure to replace C:\\path\\to\\your\\... with the actual path to your python script)
