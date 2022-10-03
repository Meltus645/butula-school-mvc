# Butula School Repository

## Welcome

Welcome to the official Butula School website development repository.

## Contribution

If you have access to this repository it means you can contribute to its development. To contribute:

1. Clone this repository
2. Create a feature branch
3. Make changes
4. Push changes to your upstream branch and make a pull request then wait for uproval and intergration of your changes.

**Note**: Do not commit environment variable, Workspace settings, interperter caches, your logs or test upload media files. Simply ignore them in the ```.gitignore``` file

```.gitignore
.vscode
.idea
.env
/env
*__pycache__/
/logs 
/uploads 
```

You can specify your ```.env``` variables in a ```.env.example``` file as:

```.env
VARIABLE_NAME=Explain this variable 
```

Define your secret keys, database settings and any other sensitive variable inside the ```.env``` file and explain them in the ```.env.example``` file so that other developers working on this project are not unnecessarily inconvenienced by your private configurations.

## Installation

After cloning the repository run the following commands from your terminal to install the required dependancies

```bash
    cd butulaschool
    pip install -r requirements.txt
```  

After the installtion create a ```.env``` file and create the variables listed in the ```.env.example``` file. After the basic setup run the command below

```bash
    flask run
```

## Development Technology

This project is implemented using:

* ```Python Flask``` - backend
* ```Flask Jinja``` - template views
* ```Flask MongoEngine``` - MongoDb flask driver

## Deployment Environment

[Development]("http://127.0.0.1:8080", "http://127.0.0.1:8080")

[Staging]("https://www.staging.butulaschool.ac.ke", "https://www.staging.butulaschool.ac.ke")

[Production]("https://www.butulaschool.ac.ke", "https://www.butulaschool.ac.ke")
