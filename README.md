**Overview**
This FastAPI project provides REST endpoints to create and retrieve wheel specification forms. The API allows you to submit wheel data and filter existing records based on form number, submitter, and date.
**Key Features**
  Create new wheel specification forms via POST requests
  Retrieve and filter wheel specification forms via GET requests
  Uses SQLAlchemy ORM for database interactions
  Modular API routing with FastAPI's APIRouter
  Returns clear success/error messages with HTTP status codes

**Setup Instructions**

**Prerequisites**
Python 3.8 or higher installed
pip package manager

**1. Clone the repository**
  git clone <your-repo-url>
  cd <your-project-folder>

**2. Install dependencies**
  pip install -r requirements.txt
  
**3. Set up environment variables**
  Configure your local database URL in .env.

**4. Run the FastAPI server locally**
  uvicorn app.main:app --reload
        (or)
  python -m uvicorn app.main:app --reload
  The API will be available at: http://127.0.0.1:8000

**5. Test API endpoints**
  Use tools like Postman or cURL to send requests to the API
  POST /api/forms/wheel-specifications to create a new form
  GET /api/forms/wheel-specifications to retrieve filtered forms
