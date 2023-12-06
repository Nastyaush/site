FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /ush
COPY requirements.txt /ush/
RUN pip install -r requirements.txt
COPY . /ush/