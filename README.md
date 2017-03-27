# harrymoreno_backend

## Usage
- install requirements `$ pip3 install -r requirements.txt`
- activate the virtualenv `$ source harrymoreno_backend`
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
