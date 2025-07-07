from app.crud.base import CRUDBase
from app.models.taxonomy import Taxonomy
from app.schemas.taxonomy import TaxonomyCreate, TaxonomyUpdate


class CRUDTaxonomy(CRUDBase[Taxonomy, TaxonomyCreate, TaxonomyUpdate]):
    ...


taxonomy = CRUDTaxonomy(Taxonomy)
