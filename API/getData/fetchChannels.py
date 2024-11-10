import os, sys
import aiohttp

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from config import API_KEY

async def fetchStatsChannelById(id : str) :
    async with aiohttp.ClientSession() as session :
        async with session.get(f'https://api.tgstat.ru/channels/stat?token={API_KEY}&channelId={id}') as req :
            return await req.json()
    