FROM python:3.8-buster
WORKDIR /task_2_microservices/master/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ ./
CMD ["python", "./master_api.py"]



