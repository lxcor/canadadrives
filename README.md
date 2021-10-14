# Canadadrives
#### BE Developer - Take home assignment
#### prepared by Alex Alves


Goal: Create an API for leaderboard application

Technology stack used:
- Ubuntu 18.04 
- Python Django 
- SQLite



- Python Django API with Django Rest Framework
- Implementation using Class based ViewSet

The following endpoints are available:

| Url                 | Method    | Action | Description                    |
|---------------------|-----------|--------|--------------------------------|
| user/               | GET       | List   | all existing users             |
| user/               | POST      | create | Create new user                |
| user/:id/           | GET       | read   | Retrieve existing user details |
| user/:id/           | DELETE    | delete | Delete existing user           |
| user/:id/increment/ | POST      | custom | Increment existing user points |
| user/:id/decrement/ | POST      | custom | Decrement existing user points |
| schema/             | GET       | schema | Generated API Schema           |

How to install the application:

1. Install required Ubuntu 18.04 software
```console
sudo apt update
sudo apt install python3-pip
sudo apt install python3-venv

sudo apt -y upgrade
```

2. Clone application code from GitHub
```console
git clone git://github.com/lxcor/canadadrives.git
```
3. Enter into application directory
```console
cd canadadrives/
```

2. Install application's virtual environment

```console
./tools.sh venv-install
```

How to test the application:

1. Run unit tests
```console
venv/bin/python3 manage.py test
```
How to run the application:

1. Run the application
```console
venv/bin/python3 manage.py runserver 0.0.0.0:8000 &
```
```

