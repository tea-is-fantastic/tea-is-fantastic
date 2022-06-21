FROM nikolaik/python-nodejs:latest

RUN npm i -g --unsafe-perm expo-cli
RUN npm cache clean --force && yarn cache clean

USER pn

ADD ./data /home/pn/data
ADD ./app /home/pn/app

RUN mkdir /home/pn/temp
VOLUME ./output /home/pn/output

WORKDIR /home/pn/app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
#RUN pip install --no-cache-dir --upgrade pip && \
#    pip install --no-cache-dir -r requirements.txt

CMD ["python", "/home/pn/app/scripts/main.py"]