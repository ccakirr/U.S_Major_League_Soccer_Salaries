
# MLS Salaries 2017 – Exploratory Data Analysis  

This project explores the **Major League Soccer 2017 player salary dataset** using **Python, Pandas, and Matplotlib**.  
The goal is to understand salary distributions, compare earnings across positions and clubs, and highlight the highest-paid players.  

---

## 📂 Dataset  
- **File**: `mls-salaries-2017.csv`  
- **Rows**: 616  
- **Columns**:  
  - `club`  
  - `first_name`  
  - `position`  
  - `base_salary`  
  - `guaranteed_compensation`  

---

## 🔎 Analysis Steps  

1. **Dataset Overview**  
   - Shape, columns, missing values  
   - Basic statistics (mean, min, max)  

2. **Salary Distributions**  
   - Histogram of base salaries  
   - Boxplot of guaranteed compensation  

3. **Position Comparison**  
   - Average salary by position (M, D, F, G)  
   - Bar chart visualization  

4. **Club Comparison**  
   - Average base salary by club  
   - Top 5 highest-paying clubs  

5. **Top Players**  
   - Top 10 by base salary  
   - Top 10 by guaranteed compensation  

6. **Base vs Guaranteed Salary**  
   - Correlation matrix  
   - Scatter plot visualization  

7. **Extra Insights**  
   - Total salary budget by club  
   - Salary breakdown by club & position  

---

## 📊 Technologies Used  
- Python 3  
- pandas  
- matplotlib  

---

## 🚀 How to Run  
```bash
pip install pandas matplotlib
python MLS_Salaries.py
```

---

## 📌 Results (Highlights)  
- Most players earn under 500k, with a few outliers earning several million.  
- Forwards generally have the highest average salaries.  
- Clubs like Toronto FC and LA Galaxy appear in the top spenders.  
- Strong positive correlation between base salary and guaranteed compensation.  

---

## 📜 License  
MIT License – feel free to use and modify. 
