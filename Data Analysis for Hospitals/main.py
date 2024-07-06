import pandas as pd

# Set the display option for maximum columns
pd.set_option('display.max_columns', 8)

# Define the file paths
general_path = 'test/general.csv'
prenatal_path = 'test/prenatal.csv'
sports_path = 'test/sports.csv'

# Read the CSV files
general_df = pd.read_csv(general_path)
prenatal_df = pd.read_csv(prenatal_path)
sports_df = pd.read_csv(sports_path)

# Print the first 20 rows of each DataFrame
print("General DataFrame:")
print(general_df.head(20))
print("\nPrenatal DataFrame:")
print(prenatal_df.head(20))
print("\nSports DataFrame:")
print(sports_df.head(20))
