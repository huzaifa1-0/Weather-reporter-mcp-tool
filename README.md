# Global Weather Reporter

**Tagline:** A lightweight, no-auth weather intelligence tool for AI agents.

## Overview
The Global Weather Reporter is a streamlined MCP tool designed for distributed AI workflows. It is deployed as a cloud service, allowing your AI assistant to fetch real-time weather conditions, temperature, and wind speed for any city on Earth without needing API keys or complex setup.

**Deployment Status:** ✅ Live on Render

## Key Features
* **🌍 Real-Time Weather:** Get current temperature, wind, and conditions instantly (`get_weather`).
* **📍 Smart Geocoding:** Automatically converts city names (e.g., "Lahore") into coordinates.
* **☁️ Cloud-Hosted:** Persistent availability via secure SSE connection.

---

## 🚀 How to Connect (For Users)

Since this tool is hosted remotely, you need a small local "bridge" script to connect it to Claude Desktop.

### Prerequisites
* Python 3.10 or higher installed.
* [Claude Desktop](https://claude.ai/download) installed.

### Step 1: Get the Connection Script
Save the code below as `client_remote.py` on your computer (or clone this repo):

```python
from fastmcp.server import create_proxy

# The URL of the deployed Weather Reporter
# Replace with your actual Render URL
RENDER_SSE_URL = "https://<YOUR-APP-NAME>[.onrender.com/sse](https://.onrender.com/sse)" 

# Initialize the proxy
mcp = create_proxy(RENDER_SSE_URL, name="Global Weather Reporter")

if __name__ == "__main__":
    mcp.run()
