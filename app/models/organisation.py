from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Organisation(Base):
    id = Column(Integer, primary_key=True, index=True)
    # parent_id = Column(String(256), nullable=False)
    # name = Column(String(256), index=True, nullable=True)

    # source = Column(String(256), nullable=True)
    submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    submitter = relationship("User", back_populates="recipes")
