import pandas as pd

# URL of Excel Files
url = "https://go.microsoft.com/fwlink/?LinkID=521962"

# Read the data from the Excel file
df = pd.read_excel(url)

# Extract the data where Sales > 50000
filtered_df = df[df[' Sales'] > 50000]

# Save the filtered data to a new Excel file. The file will be saved in the same directory as the script.
filtered_df.to_excel("filtered_sales.xlsx", index=False)