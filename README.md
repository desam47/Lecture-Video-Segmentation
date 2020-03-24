# Lecture-Video-Segmentation



Our architecture is composed of several modules where each one is responsible for one stage of processing:

API REST: architecture entrypoint where video lectures are sent to be processed.
RabbitMQ: message broker responsible for the management of the processing queues that are consumed by the processing workers
Audio Extractor: responsible for extract the audio track from the input video
Voice Activity Detector: detects and split the audio into fully voiced chunks, minimizing the silence times
ASR: Automatic Speech Recognition module
Acoustic Feature Extractor: extracts low level features (pitch, volume, pause rates, etc) from audio chunks
Flow Aggregator: aggregates the feature extraction results to be used by the topic segmentation module
Topic Segmentation: module that segments the video lecture based on the features extracted
PostgreSQL: Database used to store metadata from processing
MongoDB: Database used to store the binary files from processing
