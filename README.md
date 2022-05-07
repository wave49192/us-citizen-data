# us-citizen-data
application for us citizen database 

Tables examples  
citizen
| id |firstname | lastname | gender | jobtitle | annual_salary | state_id |
|----|--------|-----|-----|-----|-----|-----|
| 1 | Nikolia |Lewis | Male | Fabricator | 29176 | 43 |

states
| id |state_name | abbreviation |
|----|--------|-----|
| 1 | Alabama |AL|

# Setups

1.Create sample.db
```
sqlite3 sample.db --init citizen.schema
```
2.Open sample.db
```
sqlite3 sample.db
```
3.import csv file to sample.db
```
sqlite> .mode csv
sqlite> .import data/CitizensData.csv citizens
sqlite> .import data/StatesData.csv states
```
# Documents

[UML Class Diagram](https://github.com/wave49192/us-citizen-data/wiki/UML-Class-Diagram)
[Web Services](https://github.com/wave49192/us-citizen-data/wiki/Web-Services)
