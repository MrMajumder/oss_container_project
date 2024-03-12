# !/bin/bash

sudo sysdig -G 60 -W 5 -w /tmp/dump.scap container.name=<give_your_name>