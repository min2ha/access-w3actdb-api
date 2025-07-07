from pydantic import BaseModel
from .collection_target import CollectionTarget

from typing import List, Sequence
from sqlalchemy.orm import relationship


class TaxonomyBase(BaseModel):
    ttype: str
    name: str
    #parent_id: int


class TaxonomyCreate(TaxonomyBase):
    ttype: str
    name: str
    #parent_id: int


class TaxonomyUpdate(TaxonomyBase):
    name: str



# Properties shared by models stored in DB
class TaxonomyInDBBase(TaxonomyBase):
    id: int
    name: str

    #collectionsTargets: List[CollectionTarget]

    class Config:
        from_attributes = True


# Properties to return to client
class Taxonomy(TaxonomyInDBBase):
    pass


# Properties properties stored in DB
class TaxonomyInDB(TaxonomyInDBBase):
    pass


class TaxonomySearchResults(BaseModel):
    #pass
    results: Sequence[Taxonomy]
