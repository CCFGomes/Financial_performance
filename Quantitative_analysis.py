import pandas as pd

# Create a DataFrame from the provided data
data = {
    'Months': ['2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30', '2021-05-31', '2021-06-30', '2021-07-31', '2021-08-31', '2021-09-30', '2021-10-31', '2021-11-30', '2021-12-31', 'Grand Total'],
    'Sales Revenue': [903.61, 706.46, 1220.27, 761.12, 1298.37, 1112.38, 1601.57, 1001.94, 1138.03, 1482.65, 718.08, 1308.45, 13252.92],
    'Net Sales': [814.06, 636.45, 1099.34, 685.69, 1169.71, 1002.15, 1442.86, 902.65, 1025.25, 1335.72, 646.92, 1178.78, 11939.57],
    'Cost': [662.43, 322.75, 730.82, 523.67, 759.54, 717.04, 825.69, 350.34, 318.64, 501.69, 517.13, 488.03, 6717.78],
    'Net Profit': [241.18, 383.71, 489.45, 237.44, 538.83, 395.34, 775.88, 651.60, 819.38, 980.96, 200.95, 820.42, 6535.14],
    'Contribution Margin 2021': [26.7, 54.3, 40.1, 31.2, 41.5, 35.5, 48.4, 65.0, 72.0, 66.2, 28.0, 62.7, 49.3],
    'Quarter Profit 2021': ['Q1 2021', '', 'Q2 2021', '', 'Q3 2021', '', 'Q4 2021', '', '', 'Q4 2021', '', 'Q4 2021', ''],
    '% Quarter Profit 2021': ['', '', '17.05%', '', '', '', '', '', '34.38%', '', '', '30.64%', ''],
    'Revenue Growth 2021': ['', '', '-23.76%', '', '', '-15.77%', '', '', '110.42%', '-7.43%', '', '', ''],
    'Sales revenue 2020': ['', '', '', '', '', '', '', '', '', '', '', 'CA$1,185.21', '']
}

df = pd.DataFrame(data)

# Convert relevant columns to numeric
numeric_columns = ['Sales Revenue', 'Net Sales', 'Cost', 'Net Profit', 'Contribution Margin 2021', '% Quarter Profit 2021', 'Revenue Growth 2021']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Calculate total values for each column
total_values = df.sum()

# Calculate average values for numeric columns
average_values = df.mean()

# Display the total and average values
print("\nTotal Values:")
print(total_values)

print("\nAverage Values:")
print(average_values)
