# MySQL with Python: Jupyter Notebook Project

This project demonstrates how to connect Python with a MySQL database using the `mysql-connector-python` library. It covers the full workflow: connecting to the server, creating a database and tables, inserting, querying, updating, and deleting data, and displaying results using pandas DataFrames.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Notebook Workflow](#notebook-workflow)
  - [1. Installing and Importing Libraries](#1-installing-and-importing-libraries)
  - [2. Connecting to MySQL Server](#2-connecting-to-mysql-server)
  - [3. Creating a Database](#3-creating-a-database)
  - [4. Creating a Table](#4-creating-a-table)
  - [5. Inserting Data](#5-inserting-data)
  - [6. Querying Data](#6-querying-data)
  - [7. Modifying Table Structure](#7-modifying-table-structure)
  - [8. Updating and Deleting Data](#8-updating-and-deleting-data)
  - [9. Displaying Data with Pandas](#9-displaying-data-with-pandas)
- [Notes and Best Practices](#notes-and-best-practices)
- [License](#license)

---

## Project Overview

This notebook is a step-by-step guide for beginners to learn how to use Python to interact with a MySQL database. It demonstrates:

- Establishing a connection to a MySQL server and database
- Creating databases and tables
- Inserting, querying, updating, and deleting records
- Using pandas to display SQL query results

---

## Requirements

- Python 3.x
- Jupyter Notebook
- MySQL Server (running locally or remotely)
- Python packages:
  - `mysql-connector-python`
  - `pandas`

---

## Setup Instructions

1. **Install MySQL Server**  
   Make sure MySQL Server is installed and running on your machine.

2. **Install Required Python Packages**  
   Run the following in a notebook cell:
   ```python
   !pip install mysql-connector-python pandas
   ```

3. **Update Credentials**  
   Replace the MySQL username, password, and host in the notebook as needed.

---

## Notebook Workflow

### 1. Installing and Importing Libraries

- Installs `mysql-connector-python` for MySQL connectivity.
- Imports `mysql.connector` as `mc`, the `Error` class for exception handling, and `pandas` for data manipulation.

### 2. Connecting to MySQL Server

- Defines `create_server_connection()` to connect to the MySQL server (not a specific database yet).
- Handles connection errors gracefully.

### 3. Creating a Database

- Defines `create_database()` to execute a SQL query for creating a new database.
- Calls this function to create a database named `workwith`.

### 4. Creating a Table

- Defines `create_db()` to connect to a specific database.
- Defines `execute_query()` to execute SQL commands (CREATE, INSERT, UPDATE, DELETE).
- Creates an `orders` table with columns for order details.

### 5. Inserting Data

- Prepares an SQL statement to insert multiple records into the `orders` table.
- Executes the insert statement.

### 6. Querying Data

- Defines `read_query()` to execute SELECT queries and fetch results.
- Demonstrates various SELECT queries:
  - Fetching all records
  - Selecting specific columns
  - Extracting the year from a date
  - Filtering with WHERE clause
  - Ordering results

### 7. Modifying Table Structure

- Alters the `orders` table to add a new column (`age`).
- Uses `DESC` to describe the table structure.

### 8. Updating and Deleting Data

- Updates the `unit_price` for a specific order.
- Deletes a record based on `order_id`.

### 9. Displaying Data with Pandas

- Converts SQL query results into a pandas DataFrame for easy viewing and further analysis.

---

## Notes and Best Practices

- **Use `execute_query` for DDL/DML statements** (CREATE, INSERT, UPDATE, DELETE, ALTER).
- **Use `read_query` for SELECT statements**.
- Always handle exceptions to avoid crashes and to get meaningful error messages.
- Close connections and cursors when done (not shown in this notebook, but recommended for production code).
- Never hardcode sensitive credentials in production code.

---

## License

This project is for educational purposes.

---

**Author:**  
Yukti Sahu