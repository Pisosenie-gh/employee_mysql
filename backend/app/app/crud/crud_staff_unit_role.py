
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.staff_unit_role import StaffUnitRole
from app.schemas.staff_unit_role import StaffUnitRoleCreate, StaffUnitRoleUpdate


class CRUDStaffUnitRole(CRUDBase[StaffUnitRole, StaffUnitRoleCreate, StaffUnitRoleUpdate]):
    def create(
        self, db: Session, *, obj_in: StaffUnitRoleCreate
    ) -> StaffUnitRole:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj



staff_unit_role = CRUDStaffUnitRole(StaffUnitRole)


