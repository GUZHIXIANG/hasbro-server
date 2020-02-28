
default:	build

clean:
	rm -rf Makefile objs

build:
	$(MAKE) -f objs/Makefile

install:
	$(MAKE) -f objs/Makefile install

modules:
	$(MAKE) -f objs/Makefile modules

upgrade:
	/root/hasbro-server//sbin/nginx -t

	kill -USR2 `cat /root/hasbro-server//logs/nginx.pid`
	sleep 1
	test -f /root/hasbro-server//logs/nginx.pid.oldbin

	kill -QUIT `cat /root/hasbro-server//logs/nginx.pid.oldbin`
