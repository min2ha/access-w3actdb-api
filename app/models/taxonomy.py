from typing import List, Optional
from sqlalchemy import BigInteger, Column, ForeignKeyConstraint, Index, Integer, PrimaryKeyConstraint, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from app.db.base_class import Base
from app.models.target import Target
#from app.models.taxonomy import Taxonomy

    
# select * from taxonomy where parent_id isnull and ttype = 'collections'

class Taxonomy(Base):
    __tablename__ = 'taxonomy'

    __table_args__ = (
        ForeignKeyConstraint(['parent_id'], ['taxonomy.id'], name='fk_taxonomy_parent_18'),
        ForeignKeyConstraint(['taxonomytype_id'], ['taxonomy_type.id'], name='fk_taxonomy_taxonomytype_17'),
        PrimaryKeyConstraint('id', name='pk_taxonomy'),
        UniqueConstraint('url', name='uq_taxonomy_url'),
        Index('ix_taxonomy_parent_18', 'parent_id'),
        Index('ix_taxonomy_taxonomytype_17', 'taxonomytype_id')
    )

    id = Column(Integer, primary_key=True, index=True)
    #parent_id = Column(Integer, nullable=True)
    parent_id: Mapped[Optional[BigInteger]] = mapped_column(BigInteger)
    ttype = Column(String(256), nullable=False)
    name = Column(String(256), index=True, nullable=True)

    taxonomytype_id = Column(BigInteger, nullable=True)
    url = Column(String(256), nullable=False)


    #targets = relationship('app.models.target.Target', Integer, foreign_keys='collection_target', back_populates='collection')
    #target: List['Target'] = relationship('Target', secondary='collection_target', back_populates='collection')
    target: Mapped[List['Target']] = relationship('Target', back_populates='collection')
    #collectiontarget: Mapped[List['CollectionTarget']] = relationship('CollectionTarget', back_populates='collection2')

    #targets = relationship('app.models.target.Target', back_populates='collection')

    #collectiont = Column(Integer, ForeignKey('collection_target.collection_id'))

    # app.models.collection_target.CollectionTarget
    #collectiontargets = relationship('app.models.collection_target.CollectionTarget', back_populates="taxonomies")
    # taxonomies = relationship("app.models.taxonomy.Taxonomy", back_populates="collectiontargets")


    # source = Column(String(256), nullable=True)
    #submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    #submitter = relationship("User", back_populates="recipes")
    # collectionTargets = relationship(
    #     "app.models.taxonomy.Taxonomy",
    #     cascade="all,delete-orphan",
    #     back_populates="submitter",
    #     uselist=True,
    #     lazy='dynamic',
    #     primaryjoin="Taxonomy.id == app.models.collection_target.CollectionTarget.collection_id"
    # )


    class Config:
        orm_mode = True
        #from_attributes = True



# class Taxonomy(Base):
#     __tablename__ = 'taxonomy'
#     __table_args__ = (
#         ForeignKeyConstraint(['parent_id'], ['taxonomy.id'], name='fk_taxonomy_parent_18'),
#         ForeignKeyConstraint(['taxonomytype_id'], ['taxonomy_type.id'], name='fk_taxonomy_taxonomytype_17'),
#         PrimaryKeyConstraint('id', name='pk_taxonomy'),
#         UniqueConstraint('url', name='uq_taxonomy_url'),
#         Index('ix_taxonomy_parent_18', 'parent_id'),
#         Index('ix_taxonomy_taxonomytype_17', 'taxonomytype_id')
#     )

#     ttype: Mapped[str] = mapped_column(String(31))
#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)
#     url: Mapped[Optional[str]] = mapped_column(String(255))
#     created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     name: Mapped[Optional[str]] = mapped_column(String(255))
#     description: Mapped[Optional[str]] = mapped_column(Text)
#     publish: Mapped[Optional[bool]] = mapped_column(Boolean)
#     parents_all: Mapped[Optional[str]] = mapped_column(Text)
#     revision: Mapped[Optional[str]] = mapped_column(Text)
#     taxonomytype_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     parent_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     status: Mapped[Optional[str]] = mapped_column(String(255))
#     start_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     end_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     wct_at_oid: Mapped[Optional[int]] = mapped_column(BigInteger)

#     portal: Mapped[List['Portal']] = relationship('Portal', secondary='portal_license', back_populates='taxonomy')
#     parent: Mapped[Optional['Taxonomy']] = relationship('Taxonomy', remote_side=[id], back_populates='parent_reverse')
#     parent_reverse: Mapped[List['Taxonomy']] = relationship('Taxonomy', remote_side=[parent_id], back_populates='parent')
#     taxonomytype: Mapped[Optional['TaxonomyType']] = relationship('TaxonomyType', back_populates='taxonomy')
#     taxonomy: Mapped[List['Taxonomy']] = relationship('Taxonomy', secondary='taxonomy_parents_all', primaryjoin=lambda: Taxonomy.id == t_taxonomy_parents_all.c.parent_id, secondaryjoin=lambda: Taxonomy.id == t_taxonomy_parents_all.c.taxonomy_id, back_populates='parent_')
#     parent_: Mapped[List['Taxonomy']] = relationship('Taxonomy', secondary='taxonomy_parents_all', primaryjoin=lambda: Taxonomy.id == t_taxonomy_parents_all.c.taxonomy_id, secondaryjoin=lambda: Taxonomy.id == t_taxonomy_parents_all.c.parent_id, back_populates='taxonomy')
#     user: Mapped[List['Creator']] = relationship('Creator', secondary='taxonomy_user', back_populates='taxonomy')
#     target: Mapped[List['Target']] = relationship('Target', secondary='collection_target', back_populates='collection')
#     target_: Mapped[List['Target']] = relationship('Target', secondary='flag_target', back_populates='flag')
#     target1: Mapped[List['Target']] = relationship('Target', secondary='license_target', back_populates='license')
#     target2: Mapped[List['Target']] = relationship('Target', secondary='subject_target', back_populates='subject')
#     target3: Mapped[List['Target']] = relationship('Target', secondary='tag_target', back_populates='tag')
#     instance: Mapped[List['Instance']] = relationship('Instance', secondary='flag_instance', back_populates='flag')
#     license: Mapped[List['Instance']] = relationship('Instance', secondary='license_instance', back_populates='instance')
#     highlight: Mapped[List['Highlight']] = relationship('Highlight', back_populates='taxonomy')
#     target4: Mapped[List['Target']] = relationship('Target', back_populates='qaissue')
#     crawl_permission: Mapped[List['CrawlPermission']] = relationship('CrawlPermission', back_populates='license')
#     instance_: Mapped[List['Instance']] = relationship('Instance', back_populates='qaissue')
#     instance1: Mapped[List['Instance']] = relationship('Instance', secondary='tag_instance', back_populates='tag')