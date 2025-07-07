from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from app.db.base_class import Base
#from app.models.collection_target import CollectionTarget
# from app.models.taxonomy import Taxonomy
#from app.models.target import Target

class CollectionTarget(Base):
    target_id = Column(Integer, nullable=False)
    collection_id = Column(Integer, nullable=False)
    # parent_id = Column(String(256), nullable=False)
    # name = Column(String(256), index=True, nullable=True)

    # source = Column(String(256), nullable=True)
    # submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    # submitter = relationship("User", back_populates="recipes")

    # target : Target
    # taxonomy : Taxonomy
    # taxonomy_id = Column(Integer, ForeignKey("taxonomy.id"), nullable=True)
    # taxonomy_id = Column(Integer, ForeignKey("fk_collection_target_taxonomy_02"), nullable=True)
    
    # app.models.taxonomy.Taxonomy
    #taxonomies = relationship("app.models.taxonomy.Taxonomy", back_populates="collectiontargets")
    
    #targets = relationship('Target', Integer, back_populates='collection')
#    targets = relationship('Target', Integer, ForeignKey='collection_target', back_populates='collection')
    #collection: Mapped[List['Taxonomy']] = relationship('Taxonomy', back_populates='target')
    collection2: Mapped[List['Taxonomy']] = relationship('Taxonomy', back_populates='collectiontarget')

    #taxonomies = relationship('app.models.taxonomy.Taxonomy', foreign_keys='Message.user_id')

    class Config:        
        orm_mode = True
        #from_attributes = True


# t_collection_target = Table(
#     'collection_target', Base.metadata,
#     Column('target_id', BigInteger, primary_key=True, nullable=False),
#     Column('collection_id', BigInteger, primary_key=True, nullable=False),
#     ForeignKeyConstraint(['collection_id'], ['taxonomy.id'], name='fk_collection_target_taxonomy_02'),
#     ForeignKeyConstraint(['target_id'], ['target.id'], name='fk_collection_target_target_01'),
#     PrimaryKeyConstraint('target_id', 'collection_id', name='pk_collection_target')
# )