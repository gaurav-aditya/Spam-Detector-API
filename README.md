# Spam Detector API

## Instructions to Run the Code

Follow these steps to get the project up and running locally.

### 1. Clone the Repository or Create the Files

Clone this repository using the following command:

```bash
git clone https://github.com/your-username/Spam-Detector-API.git

Install Required Packages
Use pip to install the required dependencies:

bash
Copy code
pip install django djangorestframework
3. Migrate the Database
Once the packages are installed, run the following command to migrate the database:

bash
Copy code
python manage.py migrate
4. Create a Superuser
To create an admin user (superuser), use the following command:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the superuser account.

5. Populate the Database with Sample Data
To populate the database with some sample data, run the script:

bash
Copy code
python manage.py runscript populate_db
6. Run the Server
Now, you can start the development server by running:

bash
Copy code
python manage.py runserver
The server will run at http://127.0.0.1:8000/.

7. Access the API
You can access the API at the following endpoint:

http://127.0.0.1:8000/api/

Author
This project was developed by Aditya Prakash.

For more information, you can visit my Linktree.
