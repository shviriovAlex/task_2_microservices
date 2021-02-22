FROM python:3.8-buster
WORKDIR /task_2_microservices/keeper/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ ./
CMD ["python", "./keeper_api.py"]


