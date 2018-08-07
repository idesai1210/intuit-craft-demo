FROM python:2.7
ADD . /todo
WORKDIR /todo
EXPOSE 5000
DOCKER_HOST tcp://34.230.75.72:5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]