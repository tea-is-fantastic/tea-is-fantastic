FROM nikolaik/python-nodejs:latest

USER pn

RUN yarn global add expo-cli
RUN npm cache clean --force && yarn cache clean

VOLUME ./output /home/pn/output
VOLUME ./data /home/pn/data

ARG TEMP_PATH=/home/pn/temp
ARG OUTPUT_PATH=/home/pn/output
ARG DATA_PATH=/home/pn/data

ADD ./app /home/pn/app
WORKDIR /home/pn/app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "./scripts/main.py"]