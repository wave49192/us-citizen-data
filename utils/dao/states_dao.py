from models.states_models import StatesModel
from sqlalchemy.orm.session import Session


class StatesDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_states(self):
        return self.__session.query(StatesModel).all()

    def get_states_by_id(self, id):
        return self.__session.query(StatesModel).filter(StatesModel.id == id)[0]

    def get_states_by_abbreviation(self, word):
        return self.__session.query(StatesModel).filter(StatesModel.abbreviation == word)[0]
