# !/bin/bash

# start elasticsearch
sudo systemctl start elasticsearch.service
sudo systemctl enable elasticsearch.service

# start kibana
sudo systemctl start kibana
sudo systemctl enable kibana

# start logstash
sudo systemctl start logstash
sudo systemctl enable logstash
# bin/logstash -f /etc/logstash/sysdig-logstash.conf
# sudo systemctl status logstash

# start filebeat
sudo filebeat modules enable system
sudo filebeat setup --index-management -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'

sudo systemctl start filebeat
sudo systemctl enable filebeat