# Bank security panel

Helps track bank employees and visit the storehouse

### How to install

Python 3.11 should already be installed.
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Sure, here's the shorter version in English:

---

### Using Environment Variables

To run the application:

Host, Port, Name, Username, Password for database and secret key set the environment variables

```   export DB_HOST=host
   export DB_PORT=port
   export DB_NAME=name  
   export DB_USER=username
   export DB_PASSWORD=password
   export SECRET_KEY=secret_key
```

After setting, launch the application with command:

```
python manage.py runserver 0.0.0.0:8000
```

Check in browser: http://127.0.0.1:8000/

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).