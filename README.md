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


# How to run this architecture



```sh

cd Lecture-Video-Segmentation

```


```sh

sudo docker-compose up

```

Once the architecture has been initialized and all containers are running, open a new Terminal tab and enter the "Demo" folder.
 

```sh

cd Lecture-Video-Segmentation/Demo

python3 main.py
```
