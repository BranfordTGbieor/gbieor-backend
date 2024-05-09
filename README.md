# Running sightech api on your local machine 

## This is the backend api project for sightech

Clone the repo

```
git clone 
```

```
cd sightech-backend 
```

Ensure that python is installed 

create a virtual environment

```
python3 venv venv
```

activate the virtual environment

```
source venv/bin/activate
```

Install requirements

```
pip install -r requirements.txt
```

Run sqlalchemy migrations

```
flask db init

flask db migrate -m 'message'

flask db upgrade
```

Start the project

```
flask run
```

you can test the project in postman using the following endpoints

Regiister new user

```
http://127.0.0.1:5000/register

example json body

{
   "username": "john",
   "password": "test"
}
```


