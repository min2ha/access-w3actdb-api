from app.crud.base import CRUDBase
from app.models.collection_target import CollectionTarget
from app.schemas.collection_target import CollectionTargetCreate, CollectionTargetUpdate


class CRUDTarget(CRUDBase[CollectionTarget, CollectionTargetCreate, CollectionTargetUpdate]):
    ...


collectionTarget = CRUDTarget(CollectionTarget)
