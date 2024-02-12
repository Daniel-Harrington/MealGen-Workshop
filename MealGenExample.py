import pandas as pd

# Read the food data from the CSV file
df = pd.read_csv('foodsdata.csv')
df = df[['Category','Food Item','Measure','Calories','Protein','Fat','Carbs','Fibre']]
# Filter out rows containing 'nuts' (case-insensitive) in the 'Food Item' column
dfnonuts = df.where(~df['Food Item'].str.contains('nuts')).dropna()

print(dfnonuts)

meals = dfnonuts.sample(8)  # Sample 8 meals from the filtered data

while sum(meals['Protein']) < 100 or sum(meals['Calories']) < 2000 or sum(meals['Calories']) > 2001  :
    meals = dfnonuts.sample(8)

print("Here is today's meal plan: ")
print('Protien: ',sum(meals['Protein']),' Calories: ',sum(meals['Calories']))
print(meals[['Food Item','Measure','Calories', 'Protein']]  )
