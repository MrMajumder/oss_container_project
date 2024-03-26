#!/bin/bash
sudo docker build --rm -t privilege_escalation .
sudo docker run -v /tmp/:/shared/ privilege_escalation:latest /bin/sh shellscript.sh
echo "success 😈"