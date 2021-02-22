FROM python:3.8-buster
WORKDIR /task_2_microservices/master/
COPY requirements.txt .
RUN pip install -r requirements.txt
#FROM nginx:alpine
#COPY . /usr/share/nginx/html
COPY ./ ./
CMD ["python", "./master_api.py"]



