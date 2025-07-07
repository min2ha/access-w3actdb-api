from sqlalchemy import Column, Integer, String #, ForeignKey
# from sqlalchemy.orm import relationship

from app.db.base_class import Base


class SubjectTarget(Base):
    target_id = Column(Integer, nullable=False)
    subject_id = Column(Integer, nullable=False)
 
    # target : Target
    # taxonomy : Taxonomy
    taxonomy_id = Column(Integer, ForeignKey("taxonomy.id"), nullable=True)
    submitter = relationship("app.models.taxonomy.Taxonomy", back_populates="collectionTargets")

    class Config:
        from_attributes = True


t_subject_target = Table(
    'subject_target', Base.metadata,
    Column('target_id', BigInteger, primary_key=True, nullable=False),
    Column('subject_id', BigInteger, primary_key=True, nullable=False),
    ForeignKeyConstraint(['subject_id'], ['taxonomy.id'], name='fk_subject_target_taxonomy_02'),
    ForeignKeyConstraint(['target_id'], ['target.id'], name='fk_subject_target_target_01'),
    PrimaryKeyConstraint('target_id', 'subject_id', name='pk_subject_target')
)
