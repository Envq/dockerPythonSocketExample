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

Execute Server UDP in Container server
~~~
docker run -it --rm --network mynet --name server myimage python3 /workspace/serverUDP.py server 2000
~~~

Execute Client UDP in Container client
~~~
docker run -it --rm --network mynet --name client myimage python3 /workspace/clientUDP.py server 2000
~~~
Note: You must create bridge network for use the hostname server.


---
## Client on Host and Server in Container
Execute Server UDP in Container
~~~
docker run -it --rm -p 2000:2000/udp --name server myimage python3 /workspace/serverUDP.py 0.0.0.0 2000
~~~

Execute Client UDP on Host
~~~
python3 clientUDP.py localhost 2000
~~~


---
## Client in Container and Server on Host
Execute Server UDP on Host
~~~
python3 serverUDP.py localhost 2000
~~~

Execute Client UDP in Container
~~~
docker run -it --rm --name client myimage python3 /workspace/clientUDP.py host.docker.internal 2000
~~~


---
## Client on Host1 and Server on Host2
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
## Client in Host1 and Server on Container/Host2
Execute Server UDP in Container on Host2
~~~
docker run -it --rm -p 2000:2000/udp --name server myimage python3 /workspace/serverUDP.py 0.0.0.0 2000
~~~

Execute Client UDP on Host1
~~~
python3 clientUDP.py IP_HOST2 2000
~~~


---
## Client in Container/Host1 and Server on Host2 
Execute Server UDP on Host2
~~~
python3 serverUDP.py IP_HOST2 2000
~~~

Execute Client UDP in Container on Host1
~~~
docker run -it --rm --name client myimage python3 /workspace/clientUDP.py IP_HOST2 2000
~~~


---
## Client in Container/Host1 and Server in Container/Host2
Execute Server UDP in Container server on Host2
~~~
docker run -it --rm -p 2000:2000/udp --name server myimage python3 /workspace/serverUDP.py 0.0.0.0 2000
~~~

Execute Client UDP in Container client on Host1
~~~
docker run -it --rm --name client myimage python3 /workspace/clientUDP.py IP_HOST2 2000
~~~
Note: You must create bridge network for use the hostname server.

---
## EXTRA NOTES:
If you use vscode dev inside Container use:
~~~
"runArgs": [ "...other...", "--name", "APP_NAME", "-p", "2000:2000/udp"],
~~~
else if you use tcp port:
~~~
"forwardPorts": [2000]
~~~