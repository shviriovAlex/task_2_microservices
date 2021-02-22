FROM python:3.8-buster
WORKDIR /task_2_microservices/reaper/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ ./
CMD ["python", "./reaper_api.py"]



