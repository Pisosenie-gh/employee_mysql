

from sqlalchemy import Column, ForeignKey, Integer, String, Date, VARCHAR
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Grade(Base):
    __tablename__ = 'grade'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(VARCHAR(255))
    nameKz = Column(VARCHAR(255))
    isActive = Column(Integer, default=1)




