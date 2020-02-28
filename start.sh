#!/usr/bin/env bash
ulimit -u 10000
ulimit -n 4096
ulimit -d unlimited
ulimit -m unlimited
ulimit -s unlimited
ulimit -t unlimited
ulimit -v unlimited

if [ -z "${DOMINION_HOME}" ]; then
  source "$(dirname "$0")"/conf/env
fi

cat>/etc/ld.so.conf.d/python3.conf<<EOF
${DOMINION_HOME}/lib
EOF
ldconfig

if [ -n "${DOMINION_HOME}" ]; then
  uwsgi --http-socket 0.0.0.0:8000 --pythonpath ${PYTHON_HOME} \
  --chdir ${DJANGO_HOME} \
  --wsgi-file gallant/wsgi.py \
  --socket /tmp/dominion_uwsgi.socket \
  --vacuum \
  --thunder-lock \
  --enable-threads \
  --master \
  --processes 1 \
  --threads 2 \
  --pidfile uwsgi.pid \
  --py-autoreload 1 \
  --static-map /static=${DJANGO_HOME}/static/
fi

echo "${DJANGO_HOME}/gallant/static/"
echo -e   "    \033[4;33m\t======= Welcome Use Gallant Server ======\033[0m"
echo -e    "_____    -   ______   —  _______          —   "
echo -e    "|  _ \\  | | | _____| | | \_______\\       | |  "
echo -e   "| | | \\ | | | |____  | |    | |   ___    | |"
echo -e    "| |_| / | | | |___ | | |    | |  / __ \\  | |____  "
echo -e    "|____/  | | |______| | |    | |  \\_,_/ \\ |______|  "
echo -e    "                                                          "
echo -e    "  ____              __                                    "
echo -e    " / __/__  ___ _____/ /__   \033[4;34m\t® Digital Boundary (数字边界)\033[0m "
echo -e    "_\ \/ _ \/ _ / __/  '_/                                  "
echo -e    "/__ / .__/\_,_/_/ /_/\_\   \033[4;31m\t Version alpha 1.0 \033[0m"
echo -e   "   /_/                     \033[4;32m\t www.digital-boundary.com\033[0m"
