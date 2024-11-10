from fetchChannels import fetchStatsChannelById
import asyncio

methods = {
    'stats' : fetchStatsChannelById
}

async def main(users : list = [], method : str ='stats') : # Так или иначе мы применем какой-нибудь метод, иначе не будет данных (для этого будут проводиться unittest)

    assert isinstance(users, list)
    assert isinstance(method, str)

    tasks = [methods[method](use) for use in users]

    return await asyncio.gather(*tasks)