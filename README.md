## BitCamp RedberryBlogs List App ##

This Django project is a RESTful API for managing a list of blogs with categories. It utilizes Django REST Framework for building the API endpoints.

## Features

- Display a list of blogs with associated categories.
- Create a new blog (requires user authentication).
- Retrieve blogs based on category.
- User authentication via email.

## Prerequisites

Make sure you have the following installed on your machine:

- Python
- Django
- Django REST Framework


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git

2. **Install dependencies:**

   ```bash

   pip install -r requirements.txt


## Endpoints
   
. /blogs/ - Get blogs information 

. /blogs/create/ (requires authentication with email) - Create Blog

. /blogs/{id}/ - Get Blog by ID

. /categories/ - Get Categories

. /login/ - User Login


Feel free to explore and modify the script according to your needs. This project was created by Mariam Kalmakhelidze.
