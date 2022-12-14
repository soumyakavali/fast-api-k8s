import json
from typing import List
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request,status
from fastapi.encoders import jsonable_encoder
from bson import json_util

from models.findings_model import Finding, FindingResponse
router = APIRouter(prefix="/api")


@router.get("/v1/findings/", tags=["findings"],description="This will return all findings.", response_model=List[Finding])
async def get_all_finding(request:Request):
    """This will return all findings from database."""
    findings = list(request.app.database_collection.find(limit=100)) 
    return findings

@router.post("/v1/findings/", tags=["findings"],description="This will save all findings.")
async def create_new_finding(request:Request,findings_list:List[Finding]):
    """This will store all findings into database."""
    findings = jsonable_encoder(findings_list)
    new_findings = request.app.database_collection.insert_many(findings)
    response = FindingResponse(insertedIds=[],acknowledged=False)
    if new_findings.acknowledged is not True:
        response.message ="Failed to insert records."
        response.inserted_count = len(new_findings.inserted_ids)
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        response.message ="Succesfully inserted records."
        response.acknowledged = True
        response.inserted_count = len(new_findings.inserted_ids)
        
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=jsonable_encoder(response))