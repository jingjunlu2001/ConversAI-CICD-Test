FROM python:3.9

WORKDIR /conversai-docker-backend

# COPY requirements.txt .
COPY ./backend ./backend

RUN apt-get update
RUN apt install -y libgl1-mesa-glx

RUN pip install -r ./backend/requirements.txt

EXPOSE 8080

CMD ["python", "./backend/main.py"]
