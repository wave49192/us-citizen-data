from utils.us_citizen import UsCitizen
from models.citizen_models import CitizenModel

us_citizen = UsCitizen()

print(us_citizen.citizen().get_all_citizen(), '\n')
print(us_citizen.citizen().get_citizen_by_id(3), '\n')
print(us_citizen.citizen().get_citizen_by_firstname("Angelica"), '\n')
print(us_citizen.citizen().get_citizen_by_lastname("Emerson"), '\n')
print('salary more than 25000', us_citizen.citizen(
).get_citizen_by_salary_more_than(25000), '\n')
print('salary less than 25000', us_citizen.citizen(
).get_citizen_by_salary_less_than(25000), '\n')
print('Male', us_citizen.citizen().get_citizen_by_gender("Male"), '\n')
print('State id = 32', us_citizen.citizen().get_citizen_by_state_id(32), '\n')

print(us_citizen.state().get_all_states(), '\n')
print(us_citizen.state().get_states_by_id(3), '\n')
print(us_citizen.state().get_states_by_abbreviation("AR"), '\n')

# new_citizen = CitizenModel(id="160", firstname="Sirawich", lastname="Tumtamai", gender="Male",
#                            jobname="Student", annual_salary=50000, state_id=23)

# us_citizen.citizen().create_new_citizen(new_citizen)
