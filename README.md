# canadadrives

Take-home 

- Python Django API with Django Rest Framework
- Implementation using Class based ViewSet

| Path                | HTTP      | Description                   |
|---------------------|-----------|-------------------------------|
| user/               | GET       |List all existing users        |
| user/               | POST      |Create new user                |
| user/:id/           | GET       |Retrieve existing user details |
| user/:id/           | DELETE    |Delete existing user           |
| user/:id/increment/ | POST      |Increment existing user points |
| user/:id/decrement/ | POST      |Decrement existing user points |