Battery Impedance Analysis Dashboard
====================================

This Django-based web application allows users to upload CSV files containing battery performance data, process the data, and visualize the aging of batteries through various parameters, including **Electrolyte Resistance (Re)**, **Charge Transfer Resistance (Rct)**, and **Battery Impedance**.

Features
--------

*   Upload CSV files containing battery data.
*   Calculate **Battery Impedance** as the sum of **Re** and **Rct**.
*   Generate interactive plots using Plotly:
    *   **Electrolyte Resistance (Re) vs Aging**
    *   **Charge Transfer Resistance (Rct) vs Aging**
    *   **Battery Impedance vs Aging**
*   Visualize trends with a **LOWESS** trendline.

* * *

Installation
------------

### Prerequisites

*   Python 3.8+
*   Django 4.0+
*   Plotly
*   Pandas
*   Statsmodels (for trendlines)

### Step-by-Step Setup

1.  **Clone the Repository**
    
    `git clone https://github.com/kunalarya873/think-clock-innov`
    
    `cd think-clock-innov/` 
    
3.  **Set Up a Virtual Environment**
    
    `python -m venv venv`
    
    `source venv/bin/activate  # On Windows: venv\Scripts\activate` 
    
5.  **Install Dependencies**
    
    `pip install -r requirements.txt` 
    
6.  **Run Database Migrations**
    
    `python manage.py migrate` 
    
7.  **Start the Development Server**
    
    `python manage.py runserver` 
    
8.  **Access the Application** Open your web browser and navigate to:
    
    `http://127.0.0.1:8000/` 
    

* * *

Usage
-----

1.  **Upload a CSV File**:
    
    *   The CSV file should contain columns like `test_id`, `Re`, and `Rct`.
2.  **View Plots**:
    
    *   After the file is uploaded, the application calculates `Battery Impedance` and generates the following plots:
        *   **Electrolyte Resistance (Re) vs Aging**
        *   **Charge Transfer Resistance (Rct) vs Aging**
        *   **Battery Impedance vs Aging**

* * *

Project Structure
-----------------

`battery_impedance_dashboard/`
├── app/                 # Main app handling uploads and visualizations
│   ├── templates/             # HTML templates
│   │   ├── upload.html        # Upload page
│   │   ├── plot.html          # Plot display page
│   ├── views.py               # Main logic for processing and plotting
│   ├── urls.py                # App-specific URL configurations
├── static/                    # Static files
├── media/                     # Uploaded CSV files (if enabled)
├── settings.py                # Django project settings
├── urls.py                    # Project-wide URL configurations
├── manage.py                  # Django entry point
└── README.md                  # This file` 

* * *

Example CSV Format
------------------

`test_id,Re,Rct`
`1,0.05,0.10`
`2,0.06,0.11`
`3,0.07,0.12` 

* * *

Requirements
------------

*   Django
*   Pandas
*   Plotly
*   Statsmodels

Install them with:

`pip install django pandas plotly statsmodels` 

* * *
