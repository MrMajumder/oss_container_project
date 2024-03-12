# !/bin/bash

# stop filebeat
sudo systemctl stop filebeat

# stop logstash
sudo systemctl stop logstash

# stop elasticsearch
sudo systemctl stop elasticsearch.service

# stop kibana
sudo systemctl stop kibana