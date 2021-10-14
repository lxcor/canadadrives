# Leaderboard API
## BE Developer - Take home assignment

#### Prepared by Alex Alves for Canada Drives

Technology stack:
- Ubuntu 18.04 
- Python Django REST Framework 
- SQLite

The following endpoints are available:

| Url                 | Method    | Action | Description                    |
|---------------------|-----------|--------|--------------------------------|
| users/               | GET       | List   | all existing users             |
| users/               | POST      | create | Create new user                |
| users/:id/           | GET       | read   | Retrieve existing user details |
| users/:id/           | DELETE    | delete | Delete existing user           |
| users/:id/increment/ | POST      | custom | Increment existing user points |
| users/:id/decrement/ | POST      | custom | Decrement existing user points |
| schema/              | GET       | schema | Generated API Schema           |

## API Demo Server
- Click [here](http://143.110.223.227) for a demo instance of the API running.


## How to install the application:

- Install required Ubuntu 18.04 software
```console
sudo apt update
sudo apt install -y python3-pip
sudo apt install -y python3-venv
```

- Clone application code from GitHub
```console
git clone git://github.com/lxcor/canadadrives.git
```

- Enter into application's directory
```console
cd canadadrives/
```

- Create virtual environment and install requirements
```console
python3 -m venv venv
venv/bin/pip3 install --upgrade pip
venv/bin/pip install wheel
venv/bin/pip3 install -r requirements.txt
```
## How to test the application:

- Run unit tests from application's directory
```console
venv/bin/python3 manage.py test
```
## How to run the application:

- Run the application from application's directory
```console
venv/bin/python3 manage.py runserver 0.0.0.0:8000 &
```

