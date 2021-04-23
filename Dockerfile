FROM python:3.7-slim

COPY requirements.txt /
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

ENV LINK='rtsp://rtsp:password@IP:554/av_stream/ch0'

ADD ./templates/ /templates/
COPY app.py /

EXPOSE 5000

ENTRYPOINT [ "python","app.py" ]