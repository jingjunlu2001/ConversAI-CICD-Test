FROM python:3.13.1

WORKDIR /conversai-docker

# COPY requirements.txt .
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]