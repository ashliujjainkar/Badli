FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8888
ENV MONGO_URI=mongodb://mongodb:27017/
CMD ["python", "app.py"]

