# Weather Discord Bot

import requests
import discord
import os

weather_api_key = os.getenv('WEATHER_API_KEY')
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

zipcode = "50321"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={weather_api_key}&units=imperial"
response = requests.get(weather_url)
data = response.json()

weather_description = data['weather'][0]['description']
temperature = data['main']['temp'] # in Fahrenheit

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    channel = client.get_channel(732399497690480651)
    await channel.send(f"Current weather in {zipcode} is {weather_description} with a temperature of {temperature}°F")
    await client.close()

client.run(discord_bot_token)