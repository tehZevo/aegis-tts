FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

# RUN apk add git
RUN pip install -r requirements.txt

RUN apt-get -y update
RUN apt-get install libsndfile1 -y

COPY . .

EXPOSE 80

#CMD [ "tts-server" ]
#CMD [ "tts", "--list_models" ]
CMD [ "python", "-u", "main.py" ]
