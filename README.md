## Fido Test


### Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)


### Project Overview

This project is a fast api application for generating random passwords.
assword

### Features

- Python 3.10+ support
- Asynchoronous capabilities
- Basic Authentication using Username and Password
- Testing suite
- Type checking using mypy
- Readily available CRUD operations
- Linting using pylint
- Formatting using black

### Installation Guide

You need following to run this project:

- Python 3.10
- [Docker with Docker Compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/docs/#installation)

I use [asdf](https://asdf-vm.com/#/) to manage my python versions. You can use it too. However, it is only supported on Linux and macOS. For Windows, you can use something like pyenv.

Once you have installed the above and have cloned the repository, you can follow the following steps to get the project up and running:
```bash
cd backend
```

1. Create a virtual environment using poetry:

```bash
poetry shell
```

2. Install the dependencies:

```bash
poetry install
```

3. Copy the `.env.example` file to `.env` and update the values as per your needs.

4. Run the migrations:

```bash
make migrate
```

5. Run the server:

```bash
make run
```

OR

#### Using Docker

1. Run the backend app using docker compose:

```bash
docker-compose up -d
```

OR

#### Use Python directly

1. Install dependencies using pip

```bash
pip install -r requirements.txt
```

2. Run the backend app using python

```bash
python3 backend
```

The server should now be running on `http://localhost:8000` and the API documentation should be available at `http://localhost:8000/docs`.

### Usage Guide

The project is designed to be modular and scalable. There are 3 main directories in the project:

1. `core`: This directory contains the central part of this project. It contains most of the boiler plate code like security dependencies, database connections, configuration, middlewares etc. It also contains the base classes for the models, repositories, and controllers. The `core` directory is designed to be as minimal as possible and usually requires minimal attention. Overall, the `core` directory is designed to be as generic as possible.

2. `app`: This directory contains the actual application code. It contains the  controllers, and schemas for the application. The directory has following sub-directories:

   - `controllers` This is where the business logic for the application are.
   - `schemas` This is where  the schemas for the application is defined. The schemas are used for validation and serialization/deserialization of the data.

3. `api`: This directory contains the API layer of the application. It contains the API router.


#### Authentication

The authentication used is basic implementation of basic auth. When the `credential` is supplied in the `Authorization` header, the `username` and `password` is verified and the user is automatically authenticated by setting `request.user.id` using middleware. If for any endpoint you want to enforce authentication, you can use the `AuthenticationRequired` dependency. It will raise a `HTTPException` if the user is not authenticated.

#### Formatting

You can use `make format` to format the code using `black` and `isort`.

#### Linting

You can use `make lint` to lint the code using `pylint`.

#### Testing

The project contains tests for all endpoints, some of the logical components like `BasicAuth` and `AuthenticationRequired` and an example of testing complex inner components like `PasswordGeneratorController` . The tests are located in `tests/`. You can run the tests using `make test`.