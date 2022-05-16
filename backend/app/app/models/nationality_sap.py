

from sqlalchemy import Column, ForeignKey, Integer, String, Date, VARCHAR
from sqlalchemy.orm import relationship

from app.db.base_class import Base




class NationalitySap(Base):
    __tablename__ = 'nationality_sap'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(255))
    isActive = Column(Integer, default=1)
    code = Column(VARCHAR(255))



