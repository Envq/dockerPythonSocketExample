# Python client/server UDP in docker

## Configuration
Build image
~~~
docker build -t myimage .
~~~

---
## Client in Container1 and Server in Container2
Create bridge network
~~~
docker network create mynet
~~~

Execute Server UDP on Container server
~~~
docker run -it --rm --network mynet --name server myimage python3 /workspace/serverUDP.py server 2001
~~~

Execute Client UDP on Container client
~~~
docker run -it --rm --network mynet --name client myimage python3 /workspace/clientUDP.py server 2001
~~~
Note: You must create bridge network for use the hostname server

---
## Client in Host and Server in Container
Execute Server UDP on Container
~~~
docker run -it --rm -p 2002:2002/udp --name server myimage python3 /workspace/serverUDP.py 0.0.0.0 2002
~~~

Execute Client UDP on Host
~~~
python3 clientUDP.py localhost 2002
~~~

---
## Client in Container and Server in Host
Execute Server UDP on Host
~~~
python3 serverUDP.py localhost 2003
~~~

Execute Client UDP on Container
~~~
docker run -it --rm --name client myimage python3 /workspace/clientUDP.py host.docker.internal 2003
~~~


---
## Host1 client and Host2 server
Get repository on both hosts (they must be on same network). Get ipv4 of server host and execute:
~~~
python3 serverUDP.py HOST_IP PORT
~~~
Then execute the client on secondo host:
~~~
python3 clientUDP.py HOST_IP PORT
~~~
Note: HOST_IP is the ipv4 of server host, and PORT is the port selected for communication.


---
## Container/Host1 client and Container/Host2 server