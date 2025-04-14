# Transwestern Pipeline Operational Available Capacity Tracker

This project retrieves, processes, and stores operational available capacity data from the Transwestern Pipeline system into a PostgreSQL database. It downloads data from the Energy Transfer website for multiple gas days and cycles, cleans it, and loads it into a structured database.

## Features

- Downloads operational available capacity data for multiple gas days and cycles
- Cleans and validates data fields (booleans, strings, integers, floats)
- Stores processed data in a PostgreSQL database
- Processes multiple date/cycle combinations concurrently using multiprocessing

## Prerequisites

- Python 3.x
- PostgreSQL
- Required Python packages (installed automatically):
  - psycopg2
  - numpy
  - pandas

## Setup and Installation

1. Clone this repository
2. Ensure PostgreSQL is installed on your system
3. Set up the required environment variables:
   - `PG_USER`: PostgreSQL username
   - `PG_PASSWORD`: PostgreSQL password
   - `DB`: PostgreSQL database name

## Usage

Run the project with the following command:

```
PG_USER=tec_dev PG_PASSWORD=verysafe42 DB=tw_db ./run.sh
```

The script will:
1. Create a Python virtual environment if it doesn't exist
2. Install required packages
3. Start the PostgreSQL server
4. Create a database user and database if they don't exist
5. Run the data processing pipeline
6. Stop the PostgreSQL server when complete

## Data Processing Pipeline

1. **Download**: Retrieves CSV data for specified gas days and cycles
2. **Clean**: Validates and transforms data into appropriate formats
3. **Load**: Inserts processed data into the PostgreSQL database

## Project Structure

- `main.py`: Main execution script that orchestrates the data pipeline
- `data_utils.py`: Utilities for downloading and processing data
- `db_utils.py`: Database connection and operation utilities
- `create_table.sql`: SQL script to create the database table
- `run.sh`: Shell script to set up environment and run the pipeline
- `requirements.txt`: Required Python packages

---

*Note: The above section of README was generated by Claude✨ but reviewed by a Leo. AI was only used to generate redundant work, such as writing out enums. NO LOGIC WAS WRITING USE AI TOOLS*

## TODO 
- Upgrade error handling with logging
- Figure out why IF NOT EXISTS doesnt seem to be working 🤷
- Add protection for duplicate data insertion
- Add fails safe for when rows are only partialy invalid


