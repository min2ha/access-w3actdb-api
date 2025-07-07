from app.crud.base import CRUDBase
from app.models.target import Target
from app.schemas.target import TargetCreate, TargetUpdate


class CRUDTarget(CRUDBase[Target, TargetCreate, TargetUpdate]):
    ...


target = CRUDTarget(Target)
