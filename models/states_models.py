from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class StatesModel(Base):

    __tablename__ = "citizens"
    id = Column(Integer, primary_key=True, nullable=False)
    state_name = Column(Text, nullable=False)
    abbreviation = Column(Text, nullable=False)


    def __repr__(self) -> str:
        return f"<State: (id={self.id},firstname={self.state_name},abbr={self.abbreviation})>"
