from pydantic import BaseModel
from typing import List, Dict

class CSVRequest(BaseModel):
    file_base64: str

class Meta(BaseModel):
    rows: int
    columns: List[str]

class CSVResponse(BaseModel):
    status: str
    meta: Meta
    data: List[Dict[str, str]]