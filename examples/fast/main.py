import hashlib
import hmac
import json
from os import environ
from typing import Union, Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
import databases

from models import zoom_webhook_event_table

DB_USER = environ.get("POSTGRES_USER", "user")
DB_PASSWORD = environ.get("POSTGRES_PASSWORD", "password")
DB_HOST = environ.get("POSTGRES_HOST", "localhost")
DB_NAME = environ.get("POSTGRES_DB", "localhost")
DB_PORT = environ.get("POSTGRES_PORT", "5432")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+aiopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)


class ZoomWebhookEvent(BaseModel):
    event: str
    event_ts: int
    payload: dict


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/zoom/webhook/")
async def zoom_webhook(webhook_event: ZoomWebhookEvent):
    if webhook_event.event == 'endpoint.url_validation':
        message = hmac.new(bytes('idgTwzmQT06XurF2lhpiWw', 'latin-1'), msg=bytes(webhook_event.payload['plainToken'], 'latin-1'), digestmod=hashlib.sha256).hexdigest()
        return {
            'plainToken': webhook_event.payload['plainToken'],
            'encryptedToken': message
        }

    query = zoom_webhook_event_table.insert().values(
        event=webhook_event.event,
        event_ts=webhook_event.event_ts,
        payload=webhook_event.payload
    )
    webhook_id = await database.execute(query)

    return {}
