from fastapi import FastAPI

from typing import List
from database.db_operations import DBClient

from routers import findings, health_check


# Instantiate the FastAPI
app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    db_client = DBClient()
    app.mongodb_client = db_client.db_client
    app.database_collection = app.mongodb_client[db_client.db_name][db_client.db_collection]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    
app.include_router(findings.router)
app.include_router(health_check.router)