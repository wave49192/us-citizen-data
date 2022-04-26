from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.citizen_dao import CitizenDao
from utils.dao.states_dao import StatesDao


class UsCitizen:

  def __init__(self, connection_url="sqlite:///sample.db"):
    engine = create_engine(connection_url)
    session = sessionmaker(bind=engine)
    self.__db_session = session()


  def citizen(self):
    return CitizenDao(self.__db_session)

  def state(self):
    return StatesDao(self.__db_session)