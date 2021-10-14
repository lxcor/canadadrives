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

| Path                | HTTP      | Description                   |
|---------------------|-----------|-------------------------------|
| user/               | GET       |List all existing users        |
| user/               | POST      |Create new user                |
| user/:id/           | GET       |Retrieve existing user details |
| user/:id/           | DELETE    |Delete existing user           |
| user/:id/increment/ | POST      |Increment existing user points |
| user/:id/decrement/ | POST      |Decrement existing user points |
| schema/ | GET     | Dynamicaly generated API Schema |

How to install the application:

1. Install required Ubuntu 18.04 software
```console
sudo apt update
sudo apt -y upgrade
git clone git://github.com/lxcor/canadadrives.git
cd canadadrives/
./tools.sh venv-install
```

2. Clone application code from GitHub

2. Install application's virtual environment

How to start/run the application
3. Run 