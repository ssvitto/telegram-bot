FROM python:3.9

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /share

CMD ["python", "bot.py"]