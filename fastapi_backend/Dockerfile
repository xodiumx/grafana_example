FROM python:3.11

WORKDIR /src

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

RUN apt-get update && apt-get install -y wget

COPY . .

RUN ["chmod", "+x", "/src/entrypoint.sh"]