FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install Flask
RUN pip install pymongo
EXPOSE 8888
ENV MONGO_URI=mongodb://mongodb:27017/
CMD ["python", "app.py"]

