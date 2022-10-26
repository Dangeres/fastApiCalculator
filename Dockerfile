FROM python:3.10
COPY . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]