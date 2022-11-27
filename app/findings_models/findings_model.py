from typing import Optional
from pydantic import BaseModel, Field

class FindingResponse(BaseModel):
    acknowledged: str
    inserted_count: Optional[int]
    message:Optional[str]

class Resource(BaseModel):
    account:str
    env: str
    platform: str
    region: str
    resource_id: str
    resource_type: str

class Finding(BaseModel):
    id:str = Field(description="id of the finding")
    findings_version: str
    revision:str
    source: str
    resource: Resource
    severity: str
    rule: str
    state: str
    last_evaluation: str
    finding_detail: str
    finding_remediation: str
    finding_short: str
    finding_lifecycle: str
    finding_type: str
    callback_url: str
    issue_tracker_id: str
    class Config:
        allow_population_by_field_name = True
        schema_extra={
            "example":{
            "id": "test_id",
            "findings_version": "1",
            "revision": "1",
            "source": "from_source",
            "resource": {
                "resource_id": "test_id",
                "env": "dev",
                "platform": "test_platform",
                "account": "123456",
                "region": "us-west-2",
                "resource_type": "test_resource_type"
            },
            "finding_type": "Runtime",
            "state": "ACTIVE",
            "finding_lifecycle": "ACTIVE",
            "timestamp": "2022-09-30T16:42:57.901Z",
            "severity": "HIGH",
            "rule": "KUBE3",
            "finding_short": "Pod running as root",
            "finding_detail": "<remediation detail?>",
            "callback_url": "callback_url",
            "issue_tracker_id": "tracker_id",
            "last_evaluation": "test_last_evaluation",
            "finding_remediation": "test_finding_remediation"
            }
        }
