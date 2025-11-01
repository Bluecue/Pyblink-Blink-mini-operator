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
    try: ##added this, dont know how try or await works yet, but I know await belongs inside the async function
        await blink.download_videos('/home/blink', since='2018/07/04 09:34', delay=2) ## needs to be a prompt for user input, asking what date range the user would like the downloaded video from.
 blink = asyncio.run(start())
