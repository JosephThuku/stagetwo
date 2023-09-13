link to mu umf diagram: https://lucid.app/lucidchart/b6f9d156-fe09-4554-b0c8-609c89f21598/edit?viewport_loc=-3959%2C-2232%2C3772%2C1614%2C0_0&invitationId=inv_074b5b0e-3151-4fda-a532-ee738f0b69a5 
if the abve doesn't work try this: https://github.com/JosephThuku/stagetwo/blob/main/umf.pdf 
# HNG STAGE TWO TASK SOLUTION

## A Simple REST API for CRUD Operations Built with Django

### Task Overview

This project involves the development of a straightforward CRUD (Create, Read, Update, Delete) API that operates on the "person" resource.

# Endpoints

## Add a New Person

**Endpoint:** `POST /person/`

**Description:** The `POST /person/` endpoint enables the creation of a new person resource.

**Example:**
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}
```

## Retrieve All Persons

**Endpoint:** `GET /person/`

**Description:** The `GET /person/` endpoint allows you to retrieve a list of all persons in the system.

**Example Response:**
```json
[
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 30
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 25
    }
]
```

## Retrieve a Specific Person

**Endpoint:** `GET /person/{userid}/`

**Description:** The `GET /person/{userid}/` endpoint allows you to retrieve information about a specific person by providing their unique ID.

**Example Response:**
```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}
```

## Update a Person

**Endpoint:** `PUT /person/{userid}/`

**Description:** The `PUT /person/{userid}/` endpoint allows you to update information about a specific person by providing their unique ID.

**Example:**
```json
{
    "first_name": "Updated John",
    "last_name": "Updated Doe",
    "age": 31
}
```

## Partially Update a Person

**Endpoint:** `PATCH /person/{userid}/`

**Description:** The `PATCH /person/{userid}/` endpoint allows you to partially update information about a specific person by providing their unique ID and the fields to be modified.

**Example:**
```json
{
    "age": 32
}
```

## Delete a Person

**Endpoint:** `DELETE /person/{userid}/`

**Description:** The `DELETE /person/{userid}/` endpoint allows you to delete a specific person by providing their unique ID.

**Note:** Replace `{userid}` in the endpoint URLs with the actual ID of the person you want to interact with.

This API provides essential CRUD operations for managing person resources. You can use these endpoints to create, retrieve, update, and delete person records within the system.

# <b> Getting started on local deployment </b>
```markdown
# crudapi Installation Guide

To set up and deploy the api on local server follow these steps:

### 1. Clone the Repository

First, clone the Mastori repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/STAGETWO.git
```

Replace `yourusername` with your actual GitHub username if you have forked the repository.

### 2. Create and Activate a Virtual Environment

It's a good practice to create a virtual environment to isolate project dependencies. Navigate to the project directory and execute the following commands:

```bash
cd crudapi
python -m venv env
```

This will create a virtual environment named `env` in your project folder. To activate the virtual environment:

- On macOS or Linux:

    ```bash
    source env/bin/activate
    ```

- On Windows:

    ```bash
    .\env\Scripts\activate
    ```

### 3. Install Required Packages

Inside the activated virtual environment, use `pip` to install the required Python packages specified in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run database migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### 5. Create a Superuser

You may want to create a superuser account to access the Django admin panel and manage the application. Run the following command and follow the prompts:

```bash
python manage.py createsuperuser
```

### 6. Run the Server

Finally, start the development server:

```bash
python manage.py runserver
```

The crudapi application should now be running locally at `http://127.0.0.1:8000/person`. You can access the admin panel at `http://127.0.0.1:8000/admin/` and start exploring and using your Mastori project.

That's it! you are ready to go
