from email.policy import default
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .employee_status import EmployeeStatus
    from .grade import Grade
    from .marital_status import MaritalStatus
    from .military_service_attitude import MilitaryServiceAttitude
    from .nationality_gender import NationalityGender
    from .ldap_login import LdapLogin


class InternalEmployee(Base):
    __tablename__ = "internal_employee"
    id = Column(Integer, primary_key=True, index=True)
    individualId = Column(Integer)
    legalOrganizationlId = Column(Integer)
    fullnameDeclinationId = Column(Integer)
    financialAccountId = Column(Integer)
    iin = Column(VARCHAR(255))
    personnelNumber = Column(VARCHAR(255))
    lastName = Column(VARCHAR(255))
    firstName = Column(VARCHAR(255))
    middleName = Column(VARCHAR(255))
    birthDate = Column(Date)
    workStartDate = Column(Date)
    isReserveMember  = Column(Boolean)
    isInsider = Column(Boolean)
    isActive = Column(Integer, default=1)
    gender = Column(VARCHAR(255))
    statusId = Column(Integer, ForeignKey('employee_status.id'))
    gradeId = Column(Integer, ForeignKey('grade.id'))
    maritalStatusId = Column(Integer, ForeignKey('marital_status.id'))
    militaryServiceAttitudeId = Column(Integer, ForeignKey('military_service_attitude.id'))
    nationalityGenderId = Column(Integer, ForeignKey('nationality_gender.id'))
    ldapLoginId = Column(Integer, ForeignKey('ldap_login.id'), nullable=True, default=None)

    status = relationship("EmployeeStatus", backref="employee_status")
    grade = relationship("Grade", backref="grade")
    marital_status = relationship("MaritalStatus", backref="marital_status")
    militaryServiceAttitude = relationship("MilitaryServiceAttitude", backref="military_service_attitude")
    nationalityGender = relationship("NationalityGender", backref="nationality_gender")
    ldapLogin = relationship("LdapLogin", backref="ldap_login")