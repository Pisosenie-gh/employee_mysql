
from email.policy import default
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date, VARCHAR
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True, index=True)
    eGovPositionId = Column(Integer)
    nameRu = Column(VARCHAR(255))
    nameKz = Column(VARCHAR(255))
    declinationId = Column(Integer)
    isActive = Column(Integer, default=1)
