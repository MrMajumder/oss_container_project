#!/bin/bash
sudo docker build --rm -t privilege_escalation .
sudo docker run --cap-add=SYS_PTRACE -v /tmp/:/shared/ privilege_escalation:latest /bin/sh bosscript.sh
echo "success 😈"