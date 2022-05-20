FROM python:3.7-slim

COPY requirements.txt /
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

# Intelbras IM5 e IM4 
ENV LINK1='rtsp://admin:XXXXXXX@192.168.100.100:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif' 
ENV LINK2='rtsp://admin:XXXXXXX@192.168.100.101:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
# SONOFF (GK-200MP2-B)
ENV LINK3='rtsp://rtsp:password@IP:554/av_stream/ch0'

ADD ./templates/ /templates/
COPY app.py /

EXPOSE 5000

ENTRYPOINT [ "python","app.py" ]