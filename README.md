# Data Analysis & Visualization Lab

Python implementations for the lab manual "Data Handling, Statistical Analysis,
Model Building, and Visualization." Each experiment has its own folder with:

- the `.py` script (matching the lab's CODE IMPLEMENTATION section)
- `output.txt` — actual console output from running the script
- any generated plots (`.png`) or processed data files

## Structure

| Folder | Experiment |
|---|---|
| `01_library_setup` | Install & verify NumPy, SciPy, Jupyter, Statsmodels, Pandas, Matplotlib, Seaborn, Plotly, Bokeh |
| `02a_numpy_operations` | NumPy array creation, indexing, slicing, aggregation, structured arrays |
| `02b_pandas_dataframe` | Pandas DataFrame loading, cleaning, filtering, grouping, sorting |
| `02c_reading_data` | Reading CSV, Excel, and web-based data |
| `02d_iris_descriptive` | Descriptive analytics on the Iris dataset |
| `03a_univariate_analysis` | Mean, median, mode, variance, skewness, kurtosis |
| `03b_bivariate_regression` | Linear & logistic regression |
| `03c_multiple_regression` | Multiple regression (predicting BMI) |
| `03d_comparison_analysis` | Comparing UCI vs Pima dataset statistics |
| `04a_normal_curves` | Histogram + normal curve overlays |
| `04b_ztest` | Z-test on mean Glucose |
| `04c_ttest` | Independent T-test between datasets |
| `04d_anova` | One-way ANOVA between datasets |
| `06a_linear_models` | Linear regression model validation (R2, MSE, MAE) |
| `06b_logistic_models` | Logistic regression + confusion matrices |
| `06c_timeseries` | Decomposition, moving average, ARIMA forecasting |

## Data

`data/generate_datasets.py` generates the synthetic UCI-style and Pima-style
diabetes datasets, the Iris dataset, and small sample CSV/Excel files used
across the experiments (the original lab manual referenced datasets that
weren't attached, so these are reproducible synthetic stand-ins with the
same schema).

## Running

```bash
pip install numpy scipy jupyter statsmodels pandas matplotlib seaborn plotly bokeh scikit-learn openpyxl
python data/generate_datasets.py
cd 01_library_setup && python library_setup.py
# ...and so on for each folder
```
