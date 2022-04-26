from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CitizenModel(Base):
    __tablename__ = "citizens"

    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    jobname = Column(Text, nullable=False)
    annual_salary = Column(Integer, nullable=False)
    state_id = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Citizen: (id={self.id},firstname={self.firstname},lastname={self.lastname},gender={self.gender}" \
               f",jobname={self.jobname},annual_salary={self.annual_salary},state_id={self.state_id})>"
