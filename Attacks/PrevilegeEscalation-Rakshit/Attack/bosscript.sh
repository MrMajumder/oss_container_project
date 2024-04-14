#!/bin/bash
apk add strace
# ls -la shellscript.sh
strace -fvttTyy -s 256 -o /shared/stracedout.txt /bin/sh -c "cp shell /shared/shell && chmod 4777 /shared/shell"