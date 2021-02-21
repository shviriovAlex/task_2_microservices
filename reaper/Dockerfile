FROM python:3.8-buster
WORKDIR /reaper
ENV FLASK_APP=reaper_api.py
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /reaper
CMD ["python","Master.py"]