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

- cd task_2_microservices
- write command: docker-compose up --build
- run localhost:8000
- enter in link, for example, https://rabota.by/search/vacancy?area=16&fromSearchLine=true&st=searchVacancy&text=python
- enter word that you want to find
- in link search word you can enter word that you need to find in database
- in localhost:8002 you can see all data