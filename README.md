# Cuisine Hunt

Cuisine Hunt is a Django web application designed to help users search for restaurants and dishes. The application incorporates various functionalities, including data loading commands, models for restaurants and dishes, admin views, HTML templates, static files, and integration with Leaflet.js for mapping.

## Project Structure

- **search_app**: Contains the core functionalities of the application.
- **models.py**: Defines the `Restaurant` and `Dish` models.
- **admin.py**: Registers models to the Django admin interface.
- **management/commands**: Includes custom management commands (`load_data` and `load_data1`) to populate the database.
- **views.py**: Handles the logic for rendering HTML templates.
- **urls.py**: Routes URLs to the appropriate views.
- **templates/**: Contains HTML templates.
- **static/**: Stores static files such as CSS, JavaScript, and images.
- **assets/**: Includes additional assets for the application.
- **Leaflet.js**: Integrated for displaying maps.

## Installation

Follow these steps to get the project up and running:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Daws23/Cuisine-Hunt.git
   cd Cuisine-Hunt
2. **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
4. **Run Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
5. **Load Initial Data**

    - Run certain custom-created commands to load data into the db based on ORM
    ```bash

    python manage.py load_data
    python manage.py load_data1
6. **For Admin Panel**

    - To monitor the admin db changes its necessary to create a superuser to authorize it
    ```bash

    python manage.py createsuperuser
7. **Ready!**
    
    - When all is set run the server to use the website
    ```bash
    python manage.py runserver
    ```
    - To view the app go to http://127.0.0.1:8000

## Dependencies

    Apart from django and its debugging tools the following tools are also used 

1. **Folium**
    - A python package to access Leaflet.js to view data distribution geographically for initial data analysis to make sure the data is clean before proceeding to load it into the SQLite DB.

2. **Pandas**
    - A library to that makes working with structured data simple and easy to visualize.

## Conclusion 

This project provides a robust foundation for managing restaurant and dish data, integrating interactive maps, and utilizing Django's powerful features. Feel free to extend and customize the application as per your needs.

For any questions or issues, please contact Daws23 at marksamuel21bcs12@iiitkottayam.ac.in.

Happy Coding!

