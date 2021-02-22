Microservices app using Docker / docker-compose.

Includes 3 parts:

- Master:
    - launches Reaper
    - get data from Keeper
- Reaper:
    - start parsing
    - send data to the Keeper
- Keeper:
    - manages DB that stores date provided by Reaper
    - return data from DB
    
How to start:
- install requirements.txt
- setting in db.yaml
- run master_api.py, reaper_api.py, keeper_api.py