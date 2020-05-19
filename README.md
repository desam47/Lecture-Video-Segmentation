# Lecture-Video-Segmentation

This "Lecture Video Segmentation" architecture consists of a number of modules, each of which is responsible for a single stage of processing. The modules used are briefly described below:

* REST API: Entry point of this architecture where lecture videos are sent to be processed.
* RabbitMQ: Message broker responsible for managing the processing queues used by the processing workers.
* Audio Extractor: Responsible for extracting audio tracks from input lecture videos. We use scipy for Audio extrator in this module.
* Voice Activity Detector: Detects and splits the audio tracks into entirely voiced parts, reducing the duration of silence. We use WebRTC Voice Activity Detector (VAD) in this module.
* ASR: Automatic Speech Recognition module that transform spoken language into text. We use Kaldi ASR in this architecture.
* Acoustic Feature Extractor: Extracts low level features (pitch, volume, pause rates, etc) from audio blocks. We use aubio algorithm in this module.
* Flow Aggregator: Aggregates the feature extraction results to be used by the segmentation module.
* Segmentation: Module that segments the lecture video based on the extracted features. We use Word2Vec model for our segmentation algorithm.
* PostgreSQL: Database used to store metadata from processing.
* MongoDB: Database used to store the binary files from processing.

# Requirements

## Install Docker

You can download and install Docker on multiple platforms. Refer to the following link and choose the best installation path for you.

[Get Docker](https://docs.docker.com/get-docker/)

## Download Kaldi

```sh

sudo mkdir /media/kaldi_models

cd /media/kaldi_models

wget https://phon.ioc.ee/~tanela/tedlium_nnet_ms_sp_online.tgz

tar -zxvf tedlium_nnet_ms_sp_online.tgz

```

## Download word2vec

```sh

sudo mkdir /media/word2vec

cd /media/word2vec

wget --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/Code: \1\n/p'

```
This will generate a Code as an output. So, you have to type the following command:

```sh

wget --load-cookies cookies.txt 'https://docs.google.com/uc?export=download&confirm=YOURCODEID&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM' -O GoogleNews-vectors-negative300.bin.gz

```
Note: Replace YOURCODEID with your code

Then extract word2vec model,

```sh

gunzip GoogleNews-vectors-negative300.bin.gz

```
## Create Docker Container

 Finally create the docker containers. It will take some time.
 
```sh

cd Lecture-Video-Segmentation

```

```sh

docker-compose up

```

## Install python3 libraries from requirements file

```sh

cd Lecture-Video-Segmentation

```

```sh

pip3 install -r requeriments.txt

```

# How to run this architecture

## Run Docker Container

```sh

cd Lecture-Video-Segmentation

```


```sh

docker-compose up

```

Once the architecture has been initialized and all containers are running, run the main file.
 

```sh

cd Lecture-Video-Segmentation/Demo

python3 main.py
```
