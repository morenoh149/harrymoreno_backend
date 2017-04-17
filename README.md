# harrymoreno_backend

## Usage
- create environment `virtualenv -p /usr/local/bin/python3.6 harrymoreno_backend`
- activate the environment `$ source harrymoreno_backend/bin/activate `
- install requirements `$ pip3 install -r requirements.txt`
- run server `$ python3 server.py`

## Deployment
- place private key in `deploy/private_key`
- place server's ip address in `deploy/hosts`, like
```
[web]
1.1.1.1
```
- ssh in a first time `$ ssh -i deploy/private_key/<file name> user@<host ip address>`
- run `$ ansible-playbook deploy/main.yml --private-key=deploy/private_key/<file name> -i deploy/hosts`

## Thoughts
- virtualenv requires 3 commands to get started, whereas npm requires one (`npm install`)
