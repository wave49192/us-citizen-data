from utils.us_citizen import UsCitizen
from models.citizen_models import CitizenModel

us_citizen = UsCitizen()

print(us_citizen.citizen().get_all_citizen())
print(us_citizen.citizen().get_citizen_by_id(3))
print(us_citizen.citizen().get_citizen_by_firstname("Angelica"))
print(us_citizen.citizen().get_citizen_by_lastname("Emerson"))
print(us_citizen.citizen.get_citizen_by_salary_range(10000, 20000))
print(us_citizen.citizen.get_citizen_by_gender("Male"))
print(us_citizen.citizen.get_citizen_by_state_id(32))

print(us_citizen.state().get_all_states())
print(us_citizen.state().get_states_by_id(3))
print(us_citizen.state().get_states_by_abbreviation("AR"))

# new_citizen = CitizenModel(id="160", firstname="Sirawich", lastname="Tumtamai", gender="Male",
#                            jobname="Student", annual_salary=50000, state_id=23)

# us_citizen.citizen().create_new_citizen(new_citizen)
