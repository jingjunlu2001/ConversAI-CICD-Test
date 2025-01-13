FROM python:3.13.1

WORKDIR /conversai-docker-backend

# COPY requirements.txt .
COPY ./backend ./backend

RUN pip install -r ./backend/requirements.txt

EXPOSE 8000

CMD ["python", "./main.py"]
