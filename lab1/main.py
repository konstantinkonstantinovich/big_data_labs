import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

star_wars = pd.read_csv("data/star_wars.csv")
## Check first 5 lines of dataset
star_wars.head()

print("Columns names before: ", star_wars.columns.to_list())
# Standardize column names
star_wars.columns = (
    star_wars.columns
    .str.encode('ascii', 'ignore').str.decode('ascii')  # Removing strange characters
    .str.replace('(', '').str.replace(')', '') # Deleting brackets
    .str.strip()  # Remove spaces at the beginning and end
)
print("Columns names after: ", star_wars.columns.to_list())


# Remove fist line with the same columns fields
star_wars_cleaned = star_wars.iloc[1:].reset_index(drop=True)
print(star_wars_cleaned.head())

# Cleaning Movie Viewing Data
STAR_WARS_EPISODES = [
    'Star Wars: Episode II Attack of the Clones',
    'Star Wars: Episode III Revenge of the Sith',
    'Star Wars: Episode IV A New Hope',
    'Star Wars: Episode V The Empire Strikes Back',
    'Star Wars: Episode VI Return of the Jedi'
]

# Get column names from the dataframe
question_column = 'Which of the following Star Wars films have you seen? Please select all that apply.'
unnamed_columns = [question_column] + [f'Unnamed: {i}' for i in range(4, 9)]

def map_seen_movies(value):
    return value in STAR_WARS_EPISODES  # Returns True if the movie is in the list, otherwise False

# Create new columns using vectorized operation
for i, column in enumerate(unnamed_columns, 1):
    if column in star_wars_cleaned.columns:
        star_wars_cleaned[f'seen_{i}'] = star_wars_cleaned[column].apply(map_seen_movies)

print(star_wars_cleaned[['seen_1', 'seen_2', 'seen_3', 'seen_4', 'seen_5', 'seen_6']].head())

seen_movies = star_wars_cleaned[['seen_1', 'seen_2', 'seen_3', 'seen_4', 'seen_5', 'seen_6']].sum()
seen_movies.plot(kind='bar')
plt.title("Number of Viewers by Star Wars Movie")
plt.xlabel("Movie")
plt.ylabel("Number of Respondents")
plt.show()

question_column = 'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.'
unnamed_columns = [question_column] + [f'Unnamed: {i}' for i in range(10, 15)]

# Rename Unnamend columns to rankins
for i, column in enumerate(unnamed_columns, 1):
    star_wars_cleaned[f'ranking_{i}'] = star_wars_cleaned[column].astype(float)


question_column = 'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.'
unnamed_columns = [question_column] + [f'Unnamed: {i}' for i in range(16, 29)]

# Cleaning Characters attitudes
for i, column in enumerate(unnamed_columns, 1):
    star_wars_cleaned[f'character_{i}'] = star_wars_cleaned[column].astype(str)

star_wars_cleaned[[f'character_{i}' for i in range(1, 13)]].head()


# Calculate and visualize average rankings
avg_rankings = star_wars_cleaned[['ranking_1', 'ranking_2', 'ranking_3', 'ranking_4', 'ranking_5', 'ranking_6']].mean()
avg_rankings.plot(kind='bar')
plt.title("Average Star Wars Movie Rankings")
plt.xlabel("Movie")
plt.ylabel("Average Ranking (1=Best, 6=Worst)")
plt.show()

# Convert Yes/No to boolean values.
yes_no_columns = [
    "Have you seen any of the 6 films in the Star Wars franchise?",
    "Do you consider yourself to be a fan of the Star Wars film franchise?",
    "Do you consider yourself to be a fan of the Star Trek franchise?",
    "Do you consider yourself to be a fan of the Expanded Universe?",
    "Are you familiar with the Expanded Universe?"
]

for col in yes_no_columns:
    star_wars_cleaned[col] = star_wars_cleaned[col].map({"Yes": True, "No": False})

print(star_wars_cleaned.head())
