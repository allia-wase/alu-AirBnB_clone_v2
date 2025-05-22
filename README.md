📦 AirBnB Clone - The Console (MySQL + ORM)
📌 Description
This project is a continuation of the AirBnB clone project and aims to implement the database storage engine using MySQL and SQLAlchemy. It introduces the use of environment variables, ORM (Object Relational Mapping), and allows switching between file storage and database storage using the same codebase. The application supports two environments: dev and test, and is structured to support a future production setup.

🛠️ Technologies Used
Python 3.8.5

MySQL 8.0

SQLAlchemy 1.4.x

Ubuntu 20.04 LTS

unittest for testing

pycodestyle for linting

🧠 Learning Objectives
By completing this project, you should be able to:

Understand and implement unit testing in large-scale projects.

Use args and kwargs effectively in Python.

Manage function arguments by name.

Set up and manage MySQL databases and users.

Grasp the concept of ORM and apply it using SQLAlchemy.

Map Python classes to SQL tables.

Handle different storage engines with a unified codebase.

Work with environment variables for project configuration.

🔧 Environment Variables
These variables control the app configuration and database connection:

bash
Copy
Edit
export HBNB_ENV=dev
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db
🏗️ Project Structure
plaintext
Copy
Edit
.
├── models/
│   ├── base_model.py
│   ├── engine/
│   │   ├── file_storage.py
│   │   └── db_storage.py
├── tests/
│   ├── test_models/
│   │   ├── test_base_model.py
│   │   └── test_engine/
│   │       └── test_db_storage.py
├── console.py
├── setup_mysql_dev.sql
├── setup_mysql_test.sql
└── README.md
🧪 Running Tests
To run all tests:

bash
Copy
Edit
python3 -m unittest discover tests
To run a specific test file:

bash
Copy
Edit
python3 -m unittest tests/test_models/test_base_model.py
🗄️ Storage Engines
The project supports two storage engines:

FileStorage (HBNB_TYPE_STORAGE=file): Saves objects to a JSON file.

DBStorage (HBNB_TYPE_STORAGE=db): Uses MySQL and SQLAlchemy ORM for object persistence.

🐘 SQL Setup
Create the development database and user:

sql
Copy
Edit
-- setup_mysql_dev.sql
-- This script creates the development database and user with privileges.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
Repeat with changes for test environment in setup_mysql_test.sql.

✨ Authors
Group project by allia-wase
