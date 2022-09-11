# Parser nginx log
## This python script parses an NGINX access log and convert it to csv.
### Getting started
You can started it in a few ways:
1. Install git and git-core packages under a Debian or Ubuntu Linux.
```git
sudo apt-get install git git-core
```
2. Clone the repository.
```git
git clone https://github.com/OVAnton/main
```
3. Install Python 3
```bash
sudo apt-get install python3.10
```
4. Using nginx_p.py script
```bash
python3 nginx_p.py
```
### Started from Dockerfile
```git
$ docker build -t parser_nginx .
$ docker run parser_nginx 
```
