FROM python:3.7-alpine

COPY ./authenticator.py /botFM/
COPY ./weeklyArtistsTweet.py /botFM/
COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /botFM
CMD ["python3", "weeklyArtistsTweet.py"]