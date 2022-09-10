FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000 3333
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python -m pip install --upgrade pip
COPY . /code/

CMD gunicorn hackathon.wsgi --bind 0.0.0.0:$PORT