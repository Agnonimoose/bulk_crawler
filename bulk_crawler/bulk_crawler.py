import asyncio, aiohttp
from aiohttp import ClientSession
from .utils import *

async def fetch_html(url: str, **kwargs) -> str:
    resp = await ClientSession.session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    html = await resp.text()
    return html

@bulk_func_asyncer(size=8)
async def fetch_urls(url: str) -> str:
    resp = await ClientSession.session.request(method="GET", url=url)
    resp.raise_for_status()
    html = await resp.text()
    return html

async def bulk_fetch(url_list):
    return await  fetch_urls(url_list)
