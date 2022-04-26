from models.citizen_models import CitizenModel
from sqlalchemy.orm.session import Session


class CitizenDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_citizen(self):
        return self.__session.query(CitizenModel).all()

    def get_citizen_by_id(self, id):
        return self.__session.query(CitizenModel).filter(CitizenModel.id == id)[0]

    def get_citizen_by_firstname(self, firstname):
        return self.__session.query(CitizenModel).filter(CitizenModel.firstname == firstname).all()

    def get_citizen_by_lastname(self, lastname):
        return self.__session.query(CitizenModel).filter(CitizenModel.lastname == lastname).all()

    def create_new_citizen(self, citizen: CitizenModel):
        self.__session.add(citizen)
        self.__session.commit()
        print("new citizen added to the database")
