FROM ubuntu:17.10
MAINTAINER Mark Dessain

RUN apt-get update
RUN apt-get install -y python3.6 python3.6-dev python3-pip python3-tk

RUN pip3 install requests==2.18.4
RUN pip3 install numpy==1.13.0
RUN pip3 install pandas==0.22.0
RUN pip3 install jupyter==1.0.0
RUN pip3 install scipy==1.0.0
RUN pip3 install scikit-learn==0.19.1
RUN pip3 install matplotlib==2.1.2
RUN pip3 install imutils==0.4.5
RUN pip3 install Pillow==5.0.0
RUN pip3 install opencv_python==3.4.0.12
RUN pip3 install aiohttp==3.0.1

RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN pip3 install snakeviz==0.4.2

RUN apt-get install -y graphviz

RUN pip3 install gprof2dot==2017.9.19

RUN pip3 install mypy==0.560

RUN pip3 intall memory_profiler==0.52.0

WORKDIR "/home/project"

# docker run -p 8080:8080 -v $(pwd):/home/project -it playground
