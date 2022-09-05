FROM python:3.8.5
COPY . /code
WORKDIR /code
COPY requirements.txt /code
RUN mkdir /var/html
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["gunicorn", "library.wsgi:application", "--bind", "0:8000" ]
