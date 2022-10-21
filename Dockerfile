FROM python:3.8.5

#install open cv2
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx libglib2.0-0
# libgl1-mesa-glx

RUN pip install opencv-python

##install numpy
#RUN pip install numpy
#
##install pandas
#RUN pip install pandas
#
#RUN pip install slack_sdk

# install geckodriver for selenium
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver
RUN mv geckodriver /usr/local/bin/

# get firefox browser
RUN apt-get update && apt-get install -y firefox-esr

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# wait to trigger main.py execution

CMD ["python", "main.py"]