import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\stuff\Task 3\FIFA23_official_data.csv')

# Level 1: Basic Data Handling

print(df.head())
print(df.isnull().sum())
print(df.describe())
print(' Number of unique clubs =',df['Club'].nunique(),'\n','Number of unique nationalities =', df['Nationality'].nunique())
print('------------------------------------------------------------')

# Check column names
print(df.columns)

# Level 2: Filtering & Aggregation

top_10_highest_rated_players = df.sort_values(by='Overall', ascending=False).head(10)
print('top 10 highest-rated players:')
print(top_10_highest_rated_players)

all_Barcelona_payers = df[df['Club'] == 'FC Barcelona']
print('All Barcelona players:') 
print(all_Barcelona_payers)

print(df.groupby('Club')['Age'].mean())

max_age_row = df.loc[df['Age'].idxmax()]
print('Oldest player :')
print(max_age_row)

min_age_row = df.loc[df['Age'].idxmin()]
print('Youngest payer :')
print(min_age_row)

top_5_valuable_players = df.sort_values(by='Value', ascending=False).head(5)
print('Top 5 most valuable players:')
print(top_5_valuable_players)

print('------------------------------------------------------------')

# Level 3: Feature Engineering & Analysis

df['Player Experience'] = df['Age'].apply(lambda x: 'Young' if x <= 22 else 'Prime' if x <= 29 else 'Veteran')
print('Data with Player Experience:')
print(df[['Name', 'Age', 'Player Experience']].head())

df_split = df['Position'].str.split('>', expand=True)
df['Position'] = df_split[1]

most_common_position = df['Position'].mode()[0]
print('\nMost common player position:', most_common_position)

average_rating_per_nationality = df.groupby('Nationality')['Overall'].mean().sort_values(ascending=False).head(5)
print('\nTop 5 best nationalities based on average player rating:')
print(average_rating_per_nationality)

under_23 = df[df['Age'] < 23]
highest_avg_rating_clubs = under_23.groupby('Club')['Overall'].mean().sort_values(ascending=False).head(5)
print('\nClubs with the highest average player rating for players under 23:')
print(highest_avg_rating_clubs)

print('------------------------------------------------------------')

# Calculation of the average player rating for each club
average_rating_per_club = df.groupby('Club')['Overall'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 8))
sns.barplot(x=average_rating_per_club.values, y=average_rating_per_club.index, hue=average_rating_per_club.index, palette='viridis', dodge=False, legend=False)
plt.xlabel('Average Player Rating')
plt.ylabel('Club')
plt.title('Top 10 Clubs with the Highest Average Player Rating')
plt.show() # Bar chart showing the top 10 clubs with the highest average player rating

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Overall', data=df)
plt.xlabel('Age')
plt.ylabel('Overall Rating')
plt.title('Scatter Plot of Age vs. Overall Rating')
plt.show() # Scatter plot of age vs overall rating

plt.figure(figsize=(10, 6))
sns.histplot(df['Value'], bins=30, kde=True)
plt.xlabel('Player Value')
plt.ylabel('Frequency')
plt.title('Distribution of Player Values')
plt.show() # Histogram showing the distribution of player values

plt.figure(figsize=(10, 6))
sns.scatterplot(x='SprintSpeed', y='Dribbling', data=df)
plt.xlabel('SprintSpeed')
plt.ylabel('Dribbling')
plt.title('Scatter Plot of SprintSpeed vs. Dribbling')
plt.show() # Scatter plot of Pace vs Dribbling


correlation = df['SprintSpeed'].corr(df['Dribbling'])
print('Correlation between Pace and Dribbling:', correlation) # Correlation between Pace and Dribbling
