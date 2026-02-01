import os
import httpx
from fastmcp import FastMCP

# Initialize
mcp = FastMCP("Global Weather Reporter")

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get the real-time weather for any city in the world.
    Args:
        city: The name of the city (e.g. "Lahore", "New York", "Tokyo")
    """
    async with httpx.AsyncClient() as client:
        try:
            # 1. Geocoding: Get Lat/Long for the city
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
            geo_resp = await client.get(geo_url)
            geo_data = geo_resp.json()

            if "results" not in geo_data:
                return f"Error: Could not find city '{city}'."

            location = geo_data["results"][0]
            lat = location["latitude"]
            long = location["longitude"]

            # 2. Weather: Fetch data for those coordinates
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
            weather_resp = await client.get(weather_url)
            weather_data = weather_resp.json()

            current = weather_data["current_weather"]
            
            return (f"Weather in {location['name']}, {location.get('country')}:\n"
                    f"🌡️ Temp: {current['temperature']}°C\n"
                    f"💨 Wind: {current['windspeed']} km/h\n"
                    f"Conditions: Code {current['weathercode']}")

        except Exception as e:
            return f"Failed to fetch weather: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting Weather MCP on port {port}...")
    mcp.run(transport="sse", host="0.0.0.0", port=port)