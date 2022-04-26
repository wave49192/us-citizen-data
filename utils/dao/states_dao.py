from models.states_models import StatesModel
from sqlalchemy.orm.session import Session


class StatesDao:
  def __init__(self, session: Session):
    self.__session = session

  def get_all_states(self):
    return self.__session.query(StatesModel).all()