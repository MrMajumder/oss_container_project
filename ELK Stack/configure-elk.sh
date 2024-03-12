# !/bin/bash

# elastic configs
sudo cp configs/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
sudo cp configs/jvm.options /etc/elasticsearch/jvm.options

# kibana configs
sudo cp configs/kibana.yml /etc/kibana/kibana.yml
sudo ufw allow 5601/tcp # firewall rule for kibana

# logstash configs for sysdig
sudo cp configs/sysdig-logstash.conf /etc/logstash/conf.d/sysdig-logstash.conf

# filebeat configs
sudo cp configs/filebeat.yml /etc/filebeat/filebeat.yml


