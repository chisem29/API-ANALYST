
import sys
import os
import asyncio

sys.path.append(os.path.join(os.path.dirname(__file__), 'API/getData'))

from fetchMain import main

if __name__ == '__main__' :
    asyncio.run(main(['@topor']))
