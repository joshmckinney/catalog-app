# Catalog Application

A web app that allows for users to sign in via oAuth2 and create content.

**Prereqs:**

- Requires python 3+
- ```pip install -r requirements.txt```

Create Dev Account for Google oAuth2
- https://console.developers.google.com/apis
- Download and save your json as 'client_secrets.json'
- Replace data-clientid value in login.html

**How to run:**

Create the database
- ```python create_database.py```

Seed dummy info
- ```python generate_dbinfo.py```

Bring up server
- ```python server.py```
