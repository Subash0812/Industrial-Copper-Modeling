# Industrial-Copper-Modeling

# 🏭 Industrial Copper Modeling

## 📌 Project Overview
Industrial Copper Modeling is a Machine Learning project designed to solve pricing and lead-conversion challenges in the copper manufacturing industry.  
The project handles skewed and noisy data and builds robust Regression and Classification models, deployed using a Streamlit web application.

---

## 🎯 Problem Statement
The copper industry faces challenges such as:
- Skewed and noisy sales and pricing data
- Manual pricing decisions leading to inaccurate results
- Difficulty in identifying high-quality sales leads

This project addresses:
1. **Selling Price Prediction** (Regression)
2. **Lead Status Prediction** – WON or LOST (Classification)

---

## 🛠️ Tech Stack & Skills
- **Programming Language**: Python  
- **Libraries**:
  - Pandas, NumPy
  - Matplotlib, Seaborn
  - Scikit-learn
  - Streamlit
- **Machine Learning**:
  - Regression
  - Classification
  - Feature Engineering

---

## 📂 Dataset
- Source: Google Spreadsheet
- Domain: Manufacturing (Copper Industry)

### Dataset Features
- `id` – Unique transaction identifier  
- `item_date` – Transaction date  
- `quantity tons` – Quantity sold  
- `customer` – Customer identifier  
- `country` – Customer country  
- `status` – WON / LOST / others  
- `item type` – Item category  
- `application` – Usage type  
- `thickness` – Product thickness  
- `width` – Product width  
- `material_ref` – Material reference  
- `product_ref` – Product reference  
- `delivery date` – Delivery date  
- `selling_price` – Target variable  

---

## 🔍 Data Preprocessing
- Converted invalid `material_ref` values starting with `00000` to null
- Handled missing values using mean, median, or mode
- Treated outliers using:
  - IQR Method
- Handled skewness using:
  - Log Transformation
- Encoded categorical variables using:
  - One-Hot Encoding
- Removed highly correlated features using heatmaps

---

## 📊 Exploratory Data Analysis (EDA)
- Distribution analysis before and after skewness treatment
- Outlier visualization using boxplots and violin plots
- Correlation analysis using heatmaps

---

## 🤖 Model Building

### 🔹 Regression Model
- **Target**: `selling_price`
- **Model Type**: Tree-based regression models
- **Evaluation Metrics**:
  - R² Score
  - MAE
  - RMSE

### 🔹 Classification Model
- **Target**: `status` (WON / LOST)
- Filtered dataset to include only WON and LOST records
- **Algorithms Used**:
  - ExtraTreesClassifier
  - XGBoost Classifier
  - Logistic Regression
- **Evaluation Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - ROC-AUC

---

## 🌐 Streamlit Web Application
The Streamlit app allows users to:
1. Select task (Regression or Classification)
2. Enter feature values
3. Get real-time predictions

### App Features
- Applies the same preprocessing steps used during training
- Loads trained models, scalers, and encoders using pickle
- Displays predicted Selling Price or Lead Status (WON / LOST)
