from fastapi import FastAPI
import os
from discord_webhook import DiscordWebhook

app = FastAPI()

@app.get("/washer_start")
async def washer_start():
    print("Washer start")
    return {"error": None}

@app.get("/dryer_start")
async def dryer_start():
    print("Dryer start")
    return {"error": None}


@app.get("/washer_done")
async def washer_done():
    DiscordWebhook(
        url=os.environ["WASHER_WEBHOOK"],
        content='Washing machine done',
    ).execute()
    return {"error": None}

@app.get("/dryer_done")
async def dryer_done():
    DiscordWebhook(
        url=os.environ["DRYER_WEBHOOK"],
        content='Dryer done',
    ).execute()
    return {"error": None}
