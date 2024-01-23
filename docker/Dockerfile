FROM nvidia/cuda:11.0.3-base-ubuntu20.04


COPY docker/requirements.txt requirements.txt 

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    git-lfs 
    
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /work/ve
ENV HOME /work/ve
COPY tuneavideo tuneavideo
COPY data data
COPY configs configs
COPY train_tuneavideo.py train_tuneavideo.py
COPY inference.py inference.py
COPY download_models.sh download_models.sh

ENV PYTHONUNBUFFERED=1
CMD ["bash"]

