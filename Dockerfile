FROM python:latest

WORKDIR /usr/src/myapp
COPY regine.py .
RUN pip install colorama

CMD ["python", "regine.py"]
