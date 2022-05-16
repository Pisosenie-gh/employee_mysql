

from sqlalchemy import Column, Integer, String, VARCHAR

from app.db.base_class import Base


class StaffCategory(Base):
    __tablename__ = 'staff_category'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(VARCHAR(255))
    nameKz = Column(VARCHAR(255))



