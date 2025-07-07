from typing import List
from sqlalchemy import BigInteger, Column, ForeignKey, ForeignKeyConstraint, Index, Integer, PrimaryKeyConstraint, String, UniqueConstraint #, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from app.db.base_class import Base
#from app.models.taxonomy import Taxonomy


class Target(Base):
    __tablename__ = 'target'
    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['creator.id'], name='fk_target_authoruser_15'),
        ForeignKeyConstraint(['organisation_id'], ['organisation.id'], name='fk_target_organisation_16'),
        ForeignKeyConstraint(['qaissue_id'], ['taxonomy.id'], name='fk_target_qaissue_14'),
        PrimaryKeyConstraint('id', name='pk_target'),
        UniqueConstraint('url', name='uq_target_url'),
        Index('ix_target_authoruser_15', 'author_id'),
        Index('ix_target_organisation_16', 'organisation_id'),
        Index('ix_target_qaissue_14', 'qaissue_id')
    )
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    url = Column(String(256), index=True, nullable=True)
    description = Column(String(256), nullable=True)

    author_id = Column(BigInteger, nullable=False)
    organisation_id = Column(BigInteger, nullable=False)
    qaissue_id = Column(BigInteger, nullable=False)

    # submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    # submitter = relationship("User", back_populates="recipes")
    # collection = relationship('app.models.target.Target', ForeignKey("id"),  back_populates='targets')
    #collection = relationship("app.models.taxonomy.Taxonomy", ForeignKey("id"), back_populates="target")

    collection: Mapped[List['Taxonomy']] = relationship('Taxonomy', back_populates='target')



    class Config:
        orm_mode = True
        #from_attributes = True



# class Target(Base):
#     __tablename__ = 'target'
#     __table_args__ = (
#         ForeignKeyConstraint(['author_id'], ['creator.id'], name='fk_target_authoruser_15'),
#         ForeignKeyConstraint(['organisation_id'], ['organisation.id'], name='fk_target_organisation_16'),
#         ForeignKeyConstraint(['qaissue_id'], ['taxonomy.id'], name='fk_target_qaissue_14'),
#         PrimaryKeyConstraint('id', name='pk_target'),
#         UniqueConstraint('url', name='uq_target_url'),
#         Index('ix_target_authoruser_15', 'author_id'),
#         Index('ix_target_organisation_16', 'organisation_id'),
#         Index('ix_target_qaissue_14', 'qaissue_id')
#     )

#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)
#     url: Mapped[Optional[str]] = mapped_column(String(255))
#     created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     title: Mapped[Optional[str]] = mapped_column(String(255))
#     language: Mapped[Optional[str]] = mapped_column(String(255))
#     revision: Mapped[Optional[str]] = mapped_column(Text)
#     edit_url: Mapped[Optional[str]] = mapped_column(String(255))
#     qaissue_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     notes: Mapped[Optional[str]] = mapped_column(Text)
#     format: Mapped[Optional[str]] = mapped_column(String(255))
#     originating_organisation: Mapped[Optional[str]] = mapped_column(Text)
#     description: Mapped[Optional[str]] = mapped_column(Text)
#     is_in_scope_ip: Mapped[Optional[bool]] = mapped_column(Boolean)
#     is_in_scope_ip_without_license: Mapped[Optional[bool]] = mapped_column(Boolean)
#     active: Mapped[Optional[bool]] = mapped_column(Boolean)
#     author_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     flag_notes: Mapped[Optional[str]] = mapped_column(Text)
#     value: Mapped[Optional[str]] = mapped_column(Text)
#     summary: Mapped[Optional[str]] = mapped_column(Text)
#     special_dispensation: Mapped[Optional[bool]] = mapped_column(Boolean)
#     special_dispensation_reason: Mapped[Optional[str]] = mapped_column(Text)
#     is_uk_hosting: Mapped[Optional[bool]] = mapped_column(Boolean)
#     is_top_level_domain: Mapped[Optional[bool]] = mapped_column(Boolean)
#     is_uk_registration: Mapped[Optional[bool]] = mapped_column(Boolean)
#     live_site_status: Mapped[Optional[str]] = mapped_column(String(255))
#     key_site: Mapped[Optional[bool]] = mapped_column(Boolean)
#     wct_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     spt_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     keywords: Mapped[Optional[str]] = mapped_column(Text)
#     synonyms: Mapped[Optional[str]] = mapped_column(Text)
#     organisation_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     authors: Mapped[Optional[str]] = mapped_column(Text)
#     date_of_publication: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     justification: Mapped[Optional[str]] = mapped_column(Text)
#     selection_type: Mapped[Optional[str]] = mapped_column(String(255))
#     selector_notes: Mapped[Optional[str]] = mapped_column(Text)
#     archivist_notes: Mapped[Optional[str]] = mapped_column(Text)
#     legacy_site_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     uk_postal_address: Mapped[Optional[bool]] = mapped_column(Boolean)
#     uk_postal_address_url: Mapped[Optional[str]] = mapped_column(Text)
#     via_correspondence: Mapped[Optional[bool]] = mapped_column(Boolean)
#     professional_judgement: Mapped[Optional[bool]] = mapped_column(Boolean)
#     professional_judgement_exp: Mapped[Optional[str]] = mapped_column(Text)
#     no_ld_criteria_met: Mapped[Optional[bool]] = mapped_column(Boolean)
#     scope: Mapped[Optional[str]] = mapped_column(String(255))
#     depth: Mapped[Optional[str]] = mapped_column(String(255))
#     ignore_robots_txt: Mapped[Optional[bool]] = mapped_column(Boolean)
#     crawl_frequency: Mapped[Optional[str]] = mapped_column(String(255))
#     crawl_start_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     crawl_end_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     white_list: Mapped[Optional[str]] = mapped_column(Text)
#     black_list: Mapped[Optional[str]] = mapped_column(Text)
#     license_status: Mapped[Optional[str]] = mapped_column(String(255))
#     second_language: Mapped[Optional[str]] = mapped_column(String(255))
#     target_start_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     target_end_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     document_owner_id: Mapped[Optional[int]] = mapped_column(BigInteger)
#     hidden: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))
#     web_form_info: Mapped[Optional[str]] = mapped_column(Text)
#     web_form_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
#     login_page_url: Mapped[Optional[str]] = mapped_column(Text)
#     logout_url: Mapped[Optional[str]] = mapped_column(Text)
#     secret_id: Mapped[Optional[int]] = mapped_column(Integer)
#     is_wct: Mapped[Optional[bool]] = mapped_column(Boolean)
#     ignore_cookies: Mapped[Optional[bool]] = mapped_column(Boolean)
#     crawl_rate: Mapped[Optional[str]] = mapped_column(String(32))
#     parallel_queues: Mapped[Optional[str]] = mapped_column(String(32))

#     collection: Mapped[List['Taxonomy']] = relationship('Taxonomy', secondary='collection_target', back_populates='target')
#     flag: Mapped[List['Taxonomy']] = relationship('Taxonomy', secondary='flag_target', back_populates='target_')
#     license: Mapped[List['Taxonomy']] = relationship('Taxonomy', secondary='license_target', back_populates='target1')
#     subject: Mapped[List['Taxonomy']] = relationship('Taxonomy', secondary='subject_target', back_populates='target2')
#     tag: Mapped[List['Taxonomy']] = relationship('Taxonomy', secondary='tag_target', back_populates='target3')
#     author: Mapped[Optional['Creator']] = relationship('Creator', back_populates='target')
#     organisation: Mapped[Optional['Organisation']] = relationship('Organisation', back_populates='target')
#     qaissue: Mapped[Optional['Taxonomy']] = relationship('Taxonomy', back_populates='target4')
#     crawl_permission: Mapped[List['CrawlPermission']] = relationship('CrawlPermission', back_populates='target')
#     field_url: Mapped[List['FieldUrl']] = relationship('FieldUrl', back_populates='target')
#     instance: Mapped[List['Instance']] = relationship('Instance', back_populates='target')
#     lookup_entry: Mapped[List['LookupEntry']] = relationship('LookupEntry', back_populates='target')
#     watched_target: Mapped[List['WatchedTarget']] = relationship('WatchedTarget', back_populates='target')

