from fetchChannels import fetchStatsChannelById
import asyncio

methods = {
    'stats' : fetchStatsChannelById
}

async def main(users, method) :

    tasks = [methods[method](use) for use in users]

    return await asyncio.gather(*tasks)