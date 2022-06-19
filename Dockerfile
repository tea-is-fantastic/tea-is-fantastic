FROM nikolaik/python-nodejs:latest

RUN yarn global add expo-cli
RUN npm cache clean --force && yarn cache clean

USER pn

VOLUME ./output /home/pn/app/output
VOLUME ./data /home/pn/app/data

ARG TEMP_PATH=/home/pn/app/temp
ARG OUTPUT_PATH=/home/pn/output
ARG DATA_PATH=/home/pn/data

ADD ./app /home/pn/app/scripts
WORKDIR /home/pn/app

RUN git clone https://github.com/assafg/youtube-remote.git /home/pn/app/scripts

CMD ["python", "./scripts/main.py"]