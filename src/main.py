# A Bare Bones Slack API
# Illustrates basic usage of FastAPI w/ MongoDB
import os
from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
TLS_CERTIFICATEKEYFILE= os.getenv("TLS_CERTIFICATEKEYFILE")
TLS_CERTIFICATEKEYFILE_PASSWORD = os.getenv("TLS_CERTIFICATEKEYFILE_PASSWORD")
TLS_CA_FILE = os.getenv("TLS_CA_FILE")
db_client = MongoClient(MONGO_DB_URL,
                     tls=True,
                     tlsCertificateKeyFile=TLS_CERTIFICATEKEYFILE,
                     tlsCertificateKeyFilePassword= TLS_CERTIFICATEKEYFILE_PASSWORD,
                     tlsCAFile= TLS_CA_FILE)

# Message class defined in Pydantic
class Message(BaseModel):
    channel: str
    author: str
    text: str


# Instantiate the FastAPI
app = FastAPI()


@app.get("/status")
def get_status():
    """Get status of messaging server."""
    return {"status": "running"}


@app.get("/channels", response_model=List[str])
def get_channels():
    """Get all channels in list form."""
    msg_collection = db_client[DB_NAME][DB_COLLECTION]
    distinct_channel_list = msg_collection.distinct("channel")
    return distinct_channel_list
        


@app.get("/messages/{channel}", response_model=List[Message])
def get_messages(channel: str):
    """Get all messages for the specified channel."""
    msg_collection = db_client[DB_NAME][DB_COLLECTION]
    msg_list = msg_collection.find({"channel": channel})
    response_msg_list = []
    for msg in msg_list:
        response_msg_list.append(Message(**msg))
    return response_msg_list
        


@app.post("/post_message", status_code=status.HTTP_201_CREATED)
def post_message(message: Message):
    """Post a new message to the specified channel."""
    msg_collection = db_client[DB_NAME][DB_COLLECTION]
    result = msg_collection.insert_one(message.dict())
    ack = result.acknowledged
    return {"insertion": ack}
        