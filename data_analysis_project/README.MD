# Data Analysis Project

This project is a Django-based web application for uploading and analyzing CSV files. Users can upload a CSV file, and the application will perform basic data analysis, including displaying the first few rows, summary statistics, and a simple visualization.

## Features

- Upload CSV files
- Display the first few rows of the CSV
- Show summary statistics of the data
- Generate and display a histogram of the first numeric column

## Prerequisites

- Python 3.x
- Django 3.x or higher

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd data_analysis_project

2. Create a Virtual Environment

3. Install Dependencies:-

Django
pandas
matplotlib
seaborn

4. Apply Migrations:-

Apply the migrations to set up the database using python manage.py migrate then python manage.py makemigrations then python manage.py migrate

5. Run the server:-

Using python manage.py runserver

Open your web browser and go to http://127.0.0.1:8000/ to access the application.


#Brief Explanation


Views.py:-

The core functionality is implemented in the upload_file view in views.py

Templates:- 

upload.html contains the form for uploading the CSV file.
results.html displays the analysis results, including the first few rows of the data, summary statistics, and a histogram plot.

Forms.py:-

A form for file upload is defined in forms.py

Troubleshooting:-

Ensure all dependencies are installed correctly.
Check the console output for any errors during file upload and data processing.
Make sure the uploaded file is a valid CSV format.
