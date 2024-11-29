
# User Notes Management

This project provides an API for user management, including registration, authentication, and note management. It is built using FastAPI and MongoDB.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [View Notes](#view-notes)
  - [Create Note](#create-note)
  - [Update Note](#update-note)
  - [Delete Note](#delete-note)

---

## Features

- User Registration
- User Login (JWT Authentication)
- View Notes (JWT Protected)
- Create, Update, Delete Notes (JWT Protected)

## Prerequisites

- Python 3.8 or higher
- MongoDB (local or cloud instance)
- Virtual environment (optional but recommended)

---

## Setup Instructions

### 1. **Clone the repository**:
Clone this repository to your local machine.

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. **Create a virtual environment**:
Create a virtual environment to manage dependencies.

```bash
python -m venv venv
```

### 3. **Activate the virtual environment**:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 4. **Install required dependencies**:
Install the necessary Python libraries using `pip`.

```bash
pip install -r requirements.txt
```

---

## Running the Application

### 1. **Start the FastAPI application**:
Run the application using `uvicorn`.

```bash
uvicorn main:app --reload
```

This will start the FastAPI server at `http://127.0.0.1:8000`. The `--reload` flag allows the server to automatically restart on code changes.

---

## API Endpoints

### 1. **User Registration**

- **URL**: `/register`
- **Method**: `POST`
- **Description**: Registers a new user.
- **Request Body**:

  ```json
  {
    "email": "example@example.com",
    "password": "securepassword123"
  }
  ```

- **Response**:

  ```json
  {
    "message": "User registered successfully"
  }
  ```

- **Errors**:
  - `400`: If the email is already registered.

---

### 2. **View Notes**

- **URL**: `/notes`
- **Method**: `GET`
- **Description**: Retrieves the list of notes for the authenticated user.
- **Headers**:
  - `Authorization`: `Bearer <JWT_Token>`
  
- **Response**:

  ```json
  [
    {
      "note_id": "12345",
      "title": "Note Title",
      "content": "Note Content"
    }
  ]
  ```

- **Errors**:
  - `401`: If the user is not authenticated (JWT Token is missing or invalid).

---

### 3. **Create Note**

- **URL**: `/notes`
- **Method**: `POST`
- **Description**: Creates a new note for the authenticated user.
- **Headers**:
  - `Authorization`: `Bearer <JWT_Token>`
- **Request Body**:

  ```json
  {
    "title": "Note Title",
    "content": "Note Content"
  }
  ```

- **Response**:

  ```json
  {
    "message": "Note created successfully"
  }
  ```

- **Errors**:
  - `401`: If the user is not authenticated.
  
---

### 4. **Update Note**

- **URL**: `/notes/{note_id}`
- **Method**: `PUT`
- **Description**: Updates an existing note by `note_id`.
- **Path Parameter**:
  - `note_id`: The ID of the note to be updated.
- **Headers**:
  - `Authorization`: `Bearer <JWT_Token>`
- **Request Body**:

  ```json
  {
    "title": "Updated Note Title",
    "content": "Updated Note Content"
  }
  ```

- **Response**:

  ```json
  {
    "message": "Note updated successfully"
  }
  ```

- **Errors**:
  - `404`: If the note is not found or doesn't belong to the authenticated user.
  - `401`: If the user is not authenticated.

---

### 5. **Delete Note**

- **URL**: `/notes/{note_id}`
- **Method**: `DELETE`
- **Description**: Deletes a note by `note_id`.
- **Path Parameter**:
  - `note_id`: The ID of the note to be deleted.
- **Headers**:
  - `Authorization`: `Bearer <JWT_Token>`

- **Response**:

  ```json
  {
    "message": "Note deleted successfully"
  }
  ```

- **Errors**:
  - `404`: If the note is not found or doesn't belong to the authenticated user.
  - `401`: If the user is not authenticated.

---

## Testing

### 1. **Run Tests**:
To test the functionality of the API, you can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/). Alternatively, you can write unit tests using `pytest`.

---

### Additional Information

- **MongoDB**: The API is connected to a MongoDB database. Ensure your MongoDB instance is running locally or use a cloud-based service like [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
- **JWT Authentication**: This application uses JWT (JSON Web Tokens) for authentication. Ensure to include the `Authorization` header with the token in requests that require authentication.
  
---

## Troubleshooting

- If you encounter the error `ValueError: 'ObjectId' object is not iterable`, ensure that the MongoDB object IDs are properly converted into string format before returning them in the API response.
  
  Example:
  ```python
  from bson import ObjectId

  def serialize_objectid(obj):
      if isinstance(obj, ObjectId):
          return str(obj)
      raise TypeError(f"Object of type {obj.__class__.__name__} is not serializable")
  ```

---

This README provides a comprehensive guide for setting up, running, and testing the User Management API. Let me know if you need further modifications!
