from fastapi import FastAPI
import os
from discord_webhook import DiscordWebhook

washer_webhook = DiscordWebhook(
    url=os.environ["WASHER_WEBHOOK"],
    content='Washing machine done',
)
dryer_webhook = DiscordWebhook(
    url=os.environ["DRYER_WEBHOOK"],
    content='Dryer done',
)

app = FastAPI()


@app.get("/washer_done")
async def washer_done():
    washer_webhook.execute()
    return {"error": None}

@app.get("/dryer_done")
async def dryer_done():
    dryer_webhook.execute()
    return {"error": None}
