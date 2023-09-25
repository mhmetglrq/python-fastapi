from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"
    default = "not specified"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Optional[Gender] = Gender.default
    roles: Optional[List[Role]] = [Role.user]


class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    gender: Optional[Gender] = Gender.default
    roles: Optional[List[Role]] = [Role.user]
