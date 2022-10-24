# FastAPI-TODO
- A simple todo API made using python and fastapi
- A begenner friendly project to get you started in contributing to open source and making APIs

## Start contributing
You can contribute to this project under [Hacktoberfest 2022](https://hacktoberfest.com)  
Read the [Contributing Guidelines](CONTRIBUTING.md) and get started!

<br>

## Setting up

After forking and cloning the repo, to set it up on local machine, follow the given steps - 

## Creating a virtual environment

Once the repository is cloned, create a virtual environement folder in it using - 
```
pip install virtualenv
virtualenv venv
```

Then, activate the virtual environment-

### Linux
```bash
user@hostname:~/FastAPI-TODO$ source venv/bin/activate
```

### Windows
```cmd
C:\Users\Username\FastAPI-TODO> \venv\Scripts\activate
```

Refer to the [official virtualenv documentation](https://virtualenv.pypa.io) for any further help.


<br>

### Installing dependencies

To install all the dependancies for this project run the following command in your terminal -

```sh
pip install -r requirements.txt
```

<br>

### Configuring Environment Variables

Configure your environment variables by creating a `.env` file as shown in `.env.example` in the `Chitros/` directory -

#### Database variables
- `DATABASE_USERNAME` - Database username.
- `DATABASE_SERVER` - Database server name.
- `DATABASE_PASSWORD` -  Database password.
- `DATABASE_HOSTNAME` - Database host name.
- `DATABASE_NAME` - Database name.

### CORS variables
- `CORS_ORIGIN_WHITELIST` - Whitelisted URLs from which the API can receive requests.

Use `.env.example` for reference.

<br>

## Run the server!

We can start the ASGI uvicorn server with following commands -
```
uvicorn app.main:app --reload
```
**Note:** You need to be in the `FastAPI-TODO/` directory while running this command.



