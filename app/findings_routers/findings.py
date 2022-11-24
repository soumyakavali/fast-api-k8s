from typing import List
from fastapi import APIRouter
from findings_database.db_operations import DBOperations

from app.findings_models.findings_model import Finding
router = APIRouter(prefix="/api")
db_client = DBOperations()


@router.get("/findings/", tags=["findings"],description="This will return all findings.", response_model=List[Finding])
async def get_all_findings():
    """This will return all findings from database."""
    findings_collection = db_client[db_client.db_name][db_client.db_collection]
    distinct_findings_list = findings_collection.distinct("id")
    return distinct_findings_list

@router.post("/findings/", tags=["findings"],description="This will save given findings all.", response_model=List[Finding])
async def get_all_findings(findings_list:List[Finding]):
    """This will store all findings into database."""
    msg_collection = db_client[db_client.db_name][db_client.db_collection]
    result = msg_collection.insert_one(findings_list.dict())
    ack = result.acknowledged
    return {"insertion": ack}