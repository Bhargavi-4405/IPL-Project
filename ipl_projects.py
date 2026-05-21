import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("matches.csv")
print(df.head())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)
plt.figure(figsize=(10,5))
sns.countplot(x='season', data=df)
plt.title("Matches Played Per Season")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10,5))
top_teams = df['winner'].value_counts().head(10)
sns.barplot(
x=top_teams.index,
y=top_teams.values
)
plt.title("Top Winning Teams")
plt.xticks(rotation=45)
plt.ylabel("Wins")
plt.show()
plt.figure(figsize=(6,6))
df['toss_decision'].value_counts().plot.pie(
autopct='%1.1f%%'
)
plt.title("Toss Decisions")
plt.ylabel("")
plt.show()
plt.figure(figsize=(10,5))
top_players = df['player_of_match'].value_counts().head(10)
sns.barplot(
x=top_players.index,
y=top_players.values
)
plt.title("Top Player of Match Winners")
plt.xticks(rotation=75)
plt.ylabel("Awards")
plt.show()
print("Project Completed Successfully")