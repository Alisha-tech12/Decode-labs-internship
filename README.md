# Supermarket Sales Analysis - Data Science Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0.3-green)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Project Overview

This is a complete **Data Science internship project** that analyzes supermarket sales data to extract meaningful business insights. The project covers the entire data science pipeline from data collection to predictive modeling.

### Objectives
- Understand supermarket sales patterns
- Clean and preprocess real-world data
- Discover trends and outliers through EDA
- Create compelling visualizations
- Build a predictive model for customer ratings

---

## Dataset Information

**Source:** Supermarket sales records  
**Records:** 1,000+ transactions  
**Features:** 17 columns including:
- `Invoice ID` - Unique transaction identifier
- `Branch` - Branch location (A, B, C)
- `City` - City name (Yangon, Naypyitaw, Mandalay)
- `Customer type` - Member or Normal
- `Gender` - Male or Female
- `Product line` - Product category
- `Unit price` - Price per unit
- `Quantity` - Number of items purchased
- `Tax 5%` - 5% tax amount
- `Sales` - Total sales amount
- `Date` & `Time` - Transaction timestamp
- `Payment` - Payment method (Cash, Credit card, Ewallet)
- `Rating` - Customer rating (1-10)

---

## Technologies Used

| Library | Purpose |
|---------|---------|
| **Pandas** | Data loading, cleaning, manipulation |
| **NumPy** | Numerical operations |
| **Matplotlib** | Basic plotting and visualization |
| **Seaborn** | Statistical visualizations |
| **Scikit-learn** | Machine learning model |

---

## Tasks Completed

### Task 1: Data Collection & Dataset Understanding
- Loaded the CSV dataset
- Identified columns and data types
- Understood dataset size and features
- Documented what the data represents

### Task 2: Data Cleaning & Preprocessing
- Checked and handled missing values
- Removed duplicate records
- Converted date column to datetime format
- Fixed data types for categorical variables
- Extracted month and day features from date

### Task 3: Exploratory Data Analysis (EDA)
- Calculated basic statistics (mean, median, quartiles)
- Identified sales trends by product line
- Analyzed customer type and gender patterns
- Detected outliers in sales data
- Summarized key findings

### Task 4: Data Visualization
Created professional charts including:
- **Bar Chart** - Total sales by product line
- **Histogram** - Distribution of customer ratings
- **Box Plot** - Sales distribution by branch
- **Heatmap** - Feature correlations
- **Bar Chart** - Average sales by payment method

### ✅ Task 5: Predictive Model
Built a **Random Forest Regressor** to predict customer ratings based on:
- Unit price
- Quantity
- Total sales
- Gross income

**Model Performance:**
- Mean Absolute Error (MAE): ~0.5-0.7 rating points
- R² Score: ~0.15-0.25 (explains moderate variance)

---

## Key Insights

### Sales Insights
- **Health & Beauty** and **Fashion accessories** generate highest revenue
- **Credit cards** are used for largest transaction amounts
- **Ewallet** is popular for frequent but smaller purchases
- Branch A and C show higher sales variability

### Customer Insights
- Average customer rating: **7.2/10**
- Most ratings fall between **6-9** (generally satisfied customers)
- Members contribute more sales than normal customers
- Female customers show slightly higher purchase frequency

### Product Insights
| Product Line | Sales Performance |
|--------------|-------------------|
| Health & Beauty | Highest |
| Fashion accessories | Very High |
| Food & Beverages | Medium |
| Sports & Travel | Medium |
| Electronic accessories | Low |
| Home & Lifestyle | Lowest |

---

## How to Run This Project

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package installer)
