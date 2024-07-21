# DAB111 Project Group 03 - PYTHON

# Group Members
- **Araoyinbo Emmanuel** (W0852664)
- **Lingfang He** (W0868216)

# Overview
This project is part of the DAB111 course at St. Clair College. It involves storing immigration data in a SQLite database and presenting it via a Flask-based website. The project showcases our skills in Python programming, database management, and web development.

# Data Collection
- **Source**: The data used in this project comes from the Canada Immigration dataset for the year 2019.
- **Variables**: The dataset includes several variables, such as:
  - `Overall rank` (int)
  - `Country or region` (string)
  - `GDP per capita` (float)
  - `Social support` (float)
  - `Healthy life expectancy` (float)
  - `Freedom to make life choices` (float)
  - `Generosity` (float)
  - `Perceptions of corruption` (float)

# Database
- **Database Name**: `immigration_data.db`
- **Table Name**: `data_2019`
- **Table Content**: Data is imported from a CSV file named `2019.csv`.

# Website
The project includes a Flask-based website with the following pages:

# Homepage
- **Description**: The homepage provides an introduction to the project and links to the *About* and *Data* pages.
- **Link**: `/`

# About Page
- **Description**: The about page details the source of the data and provides definitions of each variable.
- **Link**: `/about`

# Data Page
- **Description**: The data page displays a sample of the immigration data. This sample showcases a subset of the Canada Immigration dataset for the year 2019.
- **Link**: `/data`

# Setup and Installation

# Prerequisites
- Python 3.x
- Flask
- pandas
- SQLite

# Installation Steps
 **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/DAB111_project_group_03.git
