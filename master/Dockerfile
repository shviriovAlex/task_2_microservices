FROM python:3.8-buster
WORKDIR /master
ENV FLASK_APP=Master.py
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /reaper
CMD ["python","reaper_api.py"]