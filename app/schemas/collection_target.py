from pydantic import BaseModel, HttpUrl
# from .taxonomy import Taxonomy
# from .target import Target

from typing import List, Sequence
from sqlalchemy.orm import relationship


class CollectionTargetBase(BaseModel):
    target_id: int
    collection_id: int
    # url: HttpUrl


class CollectionTargetCreate(CollectionTargetBase):
    target_id: int
    collection_id: int
    # url: HttpUrl
    # submitter_id: int


class CollectionTargetUpdate(CollectionTargetBase):
    target_id: int
    collection_id: int


# Properties shared by models stored in DB
class CollectionTargetInDBBase(CollectionTargetBase):
    target_id: int
    collection_id: int

    # taxonomies : List[Taxonomy]
    # targets : List[Target]
    # taxonomy: Taxonomy

    class Config:
        from_attributes = True


# Properties to return to client
class CollectionTarget(CollectionTargetInDBBase):
    pass


# Properties properties stored in DB
class CollectionTargetInDB(CollectionTargetInDBBase):
    pass


class CollectionTargetSearchResults(BaseModel):
    #pass
    results: Sequence[CollectionTarget]
