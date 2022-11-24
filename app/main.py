from fastapi import FastAPI

from typing import List

from app.findings_routers import findings, health_check

# Instantiate the FastAPI
app = FastAPI()

app.include_router(findings.router)
app.include_router(health_check.router)