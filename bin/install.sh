#!/usr/bin/env bash

# DOMINION_PATH=$(cd "$(dirname "$0")";pwd)
# apt-get -y install libpcre3 libpcre3-dev libssl-dev libffi-dev gcc make g++
# sqlversion=`sqlite3 -version 2>&1|awk '{print $1}'`
# if [ $sqlversion != "3.28.0" ];then
#    tar -zxvf ${DOMINION_PATH}/source/sqlite-autoconf-3280000.tar.gz -C ${DOMINION_PATH}/source/
#    cd ${DOMINION_PATH}/source/sqlite-autoconf-3280000
#    ./configure --prefix=/usr/local
#    make -C ${DOMINION_PATH}/source/sqlite-autoconf-3280000/
#    make install 
#    rm -rf  ${DOMINION_PATH}/source/sqlite-autoconf-3280000
#    mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
#    ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
#    export LD_LIBRARY_PATH="/usr/local/lib"
# fi

#tar -zxvf ${DOMINION_PATH}/../source/nginx-1.16.1.tar.gz -C ${DOMINION_PATH}/../source/
#cd ${DOMINION_PATH}/../source/nginx-1.16.1
# ./configure --prefix=${DOMINION_PATH}/../ --with-http_stub_status_module --with-http_ssl_module
# make -C ${DOMINION_PATH}/../source/nginx-1.16.1/
# make install 
# rm -rf  ${DOMINION_PATH}/../source/nginx-1.16.1
# rm /usr/bin/python3
# ln -s ${DOMINION_PATH}/python3.7 /usr/bin/python3