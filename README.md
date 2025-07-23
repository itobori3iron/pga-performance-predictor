# PGA Tour Performance Predictor

This project explores trends in PGA player-tournament level data.

## 📁 Project Structure


## 🔍 Goals

- Clean and model real PGA Tour data
- Predict player performance (Top 10/25 finisher?)
- Showcase full DS workflow from SQL to dashboard

## 🧰 Tools

- Python (Anaconda)
- VS Code
- SQLite
- pandas, seaborn, scikit-learn
- Streamlit (for dashboarding)

## 🛠 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run data loader
python main.py

## Day 1 Notes:

# Modeling Guide for PGA Data Analysis

This guide walks through best practices and practical steps to prepare and model the PGA dataset, particularly when dealing with fixed or mixed effects logistic regression models.

## Step 1: Inspect the Data

* Load the dataset using `pandas`.
* Use `df.head()`, `df.info()`, and `df.describe()` to get a sense of the structure, data types, and summary statistics.
* Print `df.columns` to identify variables and ensure there are no trailing whitespaces or unintended column names.

## Step 2: Check for and Handle Duplicates

* Check for duplicate rows or columns:

  ```python
  df.duplicated().sum()
  df.columns.duplicated()
  ```
* Drop any duplicate columns or rows as needed.

## Step 3: Handle Missing Data

* Use `df.isna().sum()` to count missing values per column.
* Decide on a strategy (e.g., drop rows, impute values). For modeling, dropping rows is often safest:

  ```python
  df = df.dropna(subset=['sg_putt', 'sg_arg', 'sg_app', 'sg_ott'])
  ```

## Step 4: Rename Columns (if needed)

* Ensure no spaces or special characters in column names:

  ```python
  df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
  ```

## Step 5: Convert Data Types

* Convert relevant variables to numeric if they aren't already:

  ```python
  df['made_cut'] = pd.to_numeric(df['made_cut'], errors='coerce')
  ```
* Check for and convert any categorical variables:

  ```python
  df['player_id'] = df['player_id'].astype('category')
  df['course'] = df['course'].astype('category')
  ```

## Step 6: Create a Clean Model Dataset

* Subset to relevant columns:

  ```python
  cols = ['made_cut', 'sg_putt', 'sg_arg', 'sg_app', 'sg_ott', 'player_id', 'course']
  model_data = df[cols].copy()
  ```
* Ensure no duplicate columns:

  ```python
  model_data = model_data.loc[:, ~model_data.columns.duplicated()]
  ```

## Step 7: Fit a Mixed Effects Model

* Using `statsmodels`:

  ```python
  import statsmodels.formula.api as smf
  model = smf.mixedlm("made_cut ~ sg_putt + sg_arg + sg_app + sg_ott", model_data, 
                      groups=model_data["player_id"], 
                      re_formula="~1", 
                      vc_formula={"course": "0 + C(course)"})
  result = model.fit()
  print(result.summary())
  ```

## Step 8: Interpret Results

* Look at the fixed effects coefficients to evaluate the impact of each SG metric on `made_cut`.
* Random effects (`Group Var` and `course Var`) reflect player-level and course-level variability.

## Notes

* Always verify that your predictors are numeric and have no missing values before fitting.
* Beware of multicollinearity or overly sparse categorical variables.
* Use `.astype(str)` before applying `C()` in formulas if categories are mistakenly treated as objects.

This guide is meant to be iterative. As you run into issues, log and update this guide accordingly.

