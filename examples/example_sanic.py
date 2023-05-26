import httpx
import requests
from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://wiki.nazk.gov.ua/', timeout=30)
    return text(str(response.status_code))
