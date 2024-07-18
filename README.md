# Bilateral-Solutions

# E-Commerce Troubleshooting and Utility Scripts

This repository contains three utility scripts and a SQL troubleshooting guide for an e-commerce application:

1. **Weather Data Aggregation**: Aggregates weather data from multiple records to provide insights such as average temperature and humidity.
2. **Encryption Algorithm**: Encrypts a given string by shifting each letter and reversing every second word.
3. **SQL Troubleshooting**: SQL queries to troubleshoot inventory issues where a product ordered by a customer is showing as out of stock.

## Prerequisites

- Python 3.x

## Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   There are no external dependencies required for these projects.

## Running the Scripts

### 1. Weather Data Aggregation

This script aggregates weather data from multiple records, handling missing data gracefully.

#### Usage

1. **Open the Project in VS Code**

   ```bash
   code .
   ```

2. **Run the Script**

   - Create a new file named `weather_data_aggregation.py` and copy the following code into it:

   
### 2. Encryption Algorithm

This script encrypts a given string by shifting each letter by a specified number of places and reversing every second word.

#### Usage

1. **Create a new file named `encryption_algorithm.py` and copy the following code into it:**

2. **Run the script:**

   ```bash
   python encryption_algorithm.py
   ```

### 3. SQL Troubleshooting

This guide provides SQL queries to troubleshoot an issue where a customer orders a product that shows as out of stock.

#### Usage

1. **Check Order Details:**

   ```sql
   SELECT 
       order_id,
       customer_id,
       product_id,
       quantity
   FROM 
       orders
   WHERE 
       customer_id = 'customer_id_placeholder' 
       AND order_id = 'order_id_placeholder';
   ```

2. **Check Inventory Levels:**

   ```sql
   SELECT 
       product_id,
       stock_level
   FROM 
       inventory
   WHERE 
       product_id = 'product_id_placeholder';
   ```

3. **Check Inventory Transactions:**

   ```sql
   SELECT 
       transaction_id,
       product_id,
       quantity_change,
       transaction_type,
       transaction_date
   FROM 
       inventory_transactions
   WHERE 
       product_id = 'product_id_placeholder'
   ORDER BY 
       transaction_date DESC;
   ```

4. **Check for Reserved Stock:**

   ```sql
   SELECT 
       product_id,
       reserved_quantity
   FROM 
       reserved_inventory
   WHERE 
       product_id = 'product_id_placeholder';
   ```
