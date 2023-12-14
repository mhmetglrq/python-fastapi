from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum





class News(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    description: str
    imageUrl: Optional[str]
    
