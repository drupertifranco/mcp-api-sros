from pydantic import BaseModel
from typing import List, Optional

class IPPrefix(BaseModel):
    prefix_name: str
    prefix: str

class AddIPPrefixRequest(BaseModel):
    prefix_list_name: str
    prefixes: List[IPPrefix]

class DeleteIPPrefixRequest(BaseModel):
    prefix_list_name: str
    ip_prefix: str

class ResponseMessage(BaseModel):
    message: str
    success: bool
    data: Optional[dict] = None