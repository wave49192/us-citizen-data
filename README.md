# us-citizen-data
for ssd homework

# Setups

1.Create sample.db
```
sqlite3 sample.db < citizen.schema
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
