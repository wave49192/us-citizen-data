from models.citizen_models import CitizenModel
from sqlalchemy.orm.session import Session


class CitizenDao:
  def __init__(self, session: Session):
    self.__session = session

  def get_all_cars(self):
    return self.__session.query(CitizenModel).all()