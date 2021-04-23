## Live Streaming with Flask and Open-CV in DOCKER/Buildah/Podman (Container)

This project was create to exhibit the security camera sonoff gk-200mp2-b on web browser, but it is able to support protocol RTSP to other cameras

### Build container 

	buildah bud --layers=true -t video:latest .

### Run Container 

	podman run -it --rm --name video -p5000:5000 video:latest


### Run Server Local (without container)

	pip install -r requirements.txt
	python app.py

#### Use Ip Camera/CCTV/RTSP Link

	export LINK="rtsp://username:password@camera_ip_address:554 user=username_password='password'_channel=channel_number_stream=0.sdp"

####  Example RTSP Link

	export LINK="rtsp://username:password@camera_ip_address:554 user=username_password='password'_channel=channel_number_stream=0.sdp"

	cv2.VideoCapture(LINK)

#### Display the resulting frame in browser

	cv2.imencode('.jpg', frame)[1].tobytes()                 

## Or this one

	net , buffer = cv2.imencode('.jpg', frame)
	buffer.tobytes()              


## Credit

	Learn More about Streaming with flask [link](https://blog.miguelgrinberg.com/post/video-streaming-with-flask)
