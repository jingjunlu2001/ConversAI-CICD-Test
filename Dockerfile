FROM python:3.13.1

WORKDIR /conversai-docker-backend

# COPY requirements.txt .
COPY ./backend ./backend

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
