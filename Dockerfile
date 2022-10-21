FROM python:3.8.5

#install open cv2
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev libgl1-mesa-glx
# libgl1-mesa-glx

RUN pip install opencv-python

#install numpy
RUN pip install numpy

#install pandas
RUN pip install pandas

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# wait to trigger main.py execution

CMD ["python", "main.py"]