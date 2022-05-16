

from sqlalchemy import Column, Integer, String, VARCHAR

from app.db.base_class import Base


class StaffUnitRole(Base):
    __tablename__ = 'staff_unit_role'

    id = Column(Integer, primary_key=True, index=True)
    employeeFuncRoleSpecId = Column(Integer)
    nameRu = Column(VARCHAR(255))
    nameKz = Column(VARCHAR(255))
    isActive = Column(Integer, default=1)


