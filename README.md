# DatabaseHW3

This project demonstrates how to connect PostgreSQL with Flask and perform basic operations, including inserting new data and displaying unique fruits from two tables in JSON format.

## Quick Start

### Local Test Setup

First, ensure you have Python 3 and PostgreSQL installed on your system. You may also need to install a Python virtual environment. 

To install a virtual environment, run:

```
sudo apt-get install python3-venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

Activate the environment for mac:
```
source python_venv/bin/activate
```

Or for windows:
```
.\python_venv\Scripts\activate
```

### Setting Up the Databases

Before running the application, ensure you have the required tables in your PostgreSQL database. You can run the following SQL commands:
```sql
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
        fruit_a VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');

```

### Environment Variables

Create a file named .env in the root of your project directory and include the following content:
```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```
Make sure to replace your_database_name, your_database_user, and your_database_password with your actual PostgreSQL database credentials

### API endpoints
  * To insert a new fruit ('Cherry') into basket_a:
    * Go to: http://127.0.0.1:5000/api/update_basket_a
    * Response will be in JSON format and look like
    ```
    {
    "status": "Success!"
    }
    ```
  * To get unique fruits from basket_a and basket_b:
    * Go to: http://127.0.0.1:5000/api/unique
    * Response will be in JSON format and look like
    ```
    {
    "status": "Success!",
    "unique_fruits_a": ["Banana", "Cucumber", "Cherry"],
    "unique_fruits_b": ["Watermelon", "Pear"]
    }
    ```

### Team Members
  * Joshua House
  * Hunter Kelly
