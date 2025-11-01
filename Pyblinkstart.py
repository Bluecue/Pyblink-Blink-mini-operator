## This was taken from fronzbots repository as a suggestion for logging in to blink servers.

import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink

async def start():
    blink = Blink(session=ClientSession())
    try:
        await blink.start()
    except BlinkTwoFARequiredError:
        await blink.prompt_2fa()
    return blink
    try:
        await blink.download_videos('/home/blink', since='2018/07/04 09:34', delay=2) 
 blink = asyncio.run(start())
