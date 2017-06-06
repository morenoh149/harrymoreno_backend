# harrymoreno_backend

## Usage
- create environment `virtualenv -p /usr/local/bin/python3.6 env`
- activate the environment `$ source env/bin/activate `
- install requirements `$ pip3 install -r requirements.txt`
- run server `$ python3 server.py`

## Deployment

### local
- `ansible-playbook -i "localhost," -c local deploy/main.yml`
- TODO

### AWS
- place private key in `deploy/private_key`
- place server's ip address in `deploy/hosts`, like below
```
[web]
1.1.1.1
```
- set permissions on file `chmod 400 deploy/private_key/<file name>`
- set permissions on directory `chmod 700 deploy/private_key`
- ssh in a first time `$ ssh -i deploy/private_key/<file name> ubuntu@<host ip address>`
- run `$ ansible-playbook deploy/main.yml --private-key=deploy/private_key/<file name> -i deploy/hosts -u ubuntu`

## Thoughts
- virtualenv requires 3 commands to get started, whereas npm requires one (`npm install`)
