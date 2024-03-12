# !/bin/bash

# dependencies
sudo apt-get install openjdk-8-jdk
sudo apt-get install nginx
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add - # elastic repo
sudo apt-get install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee –a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt-get update
sudo apt-get install ufw

# install elasticsearch
sudo apt-get install elasticsearch

# install kibana
sudo apt-get install kibana

# install logstash
sudo apt-get install logstash

# install filebeat
sudo apt-get install filebeat

