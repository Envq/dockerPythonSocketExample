# Python client/server UDP in docker

## Configuration
Build image
~~~
docker build -t myimage .
~~~

---
## Container1 client and Container2 server
Create bridge network
~~~
docker network create mynet
~~~

Execute Server UDP on container server
~~~
docker run -it --rm --network mynet --name server myimage python3 /workspace/serverUDP.py server 2001
~~~

Execute Client UDP on container client
~~~
docker run -it --rm --network mynet --name client myimage python3 /workspace/clientUDP.py server 2001
~~~
Note: You must create bridge network for use the hostname server

---
## Host client and Container server
Execute Server UDP on container
~~~
docker run -it --rm -p 2002:2002/udp --name server myimage python3 /workspace/serverUDP.py 0.0.0.0 2002
~~~

Execute Client UDP on host
~~~
python3 clientUDP.py localhost 2002
~~~
Note: You can't do "Host server and Container client"