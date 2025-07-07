from pydantic import BaseModel, HttpUrl

from typing import Sequence


class TargetBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class TargetCreate(TargetBase):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int


class TargetUpdate(TargetBase):
    label: str


# Properties shared by models stored in DB
class TargetInDBBase(TargetBase):
    id: int
    submitter_id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Target(TargetInDBBase):
    pass


# Properties properties stored in DB
class TargetInDB(TargetInDBBase):
    pass


class TargetSearchResults(BaseModel):
    #pass
    results: Sequence[Target]
