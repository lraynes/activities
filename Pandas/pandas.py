import pandas as pd

# Then create a Pandas Series from a raw list
data_series = pd.Series(["UC Irvine", "UCLA", "UC Berkley", "UC Riverside", "UC Davis"])
data_series

# Convert a list of dictionarys into a dataframe
states_dicts = [{"STATE": "California", "ABBREVIATION" : "CA"},
                {"STATE": "New York", "ABBREVIATION": "NY"}]
dataframe_states = pd.DataFrame(states_dicts)
dataframe_states

# Convert a single dictionary containing list into dataframe
dataframe = pd.DataFrame(
    {
        "Dynasty": ["Early Dynastic Period", "Old Kingdom"],
        "Pharoh": ["Thinis", "Memphis"]
    }
)
dataframe

# Use Pandas to read data
# Header shows first 5 rows only
data_file_pd = pd.read_csv(data_file)
data_file_pd.head()

# Dislay a statistical overview of the DataFrame
# Count, mean, std dev, min, 25%, 50%, 75%, max
data_file_pd.describe()

# Reference a single column within a DataFrame
data_file_pd["Amount"].head()

# Reference multiple columns within a DataFrame  - note the extra brackets
data_file_pd[["Amount", "Gender"]].head()

# The mean method averages the series
average = data_file_pd["Amount"].mean()
average

# The sum method adds every entry in the series
total = data_file_pd["Amount"].sum()
total

# The unique method shows every element of the series that appears only once
unique = data_file_pd["Last Name"].unique()
unique

# The value_counts method counts unique values in a column
count = data_file_pd["Gender"].value_counts()
count

# Collecting a list of all columns within the DataFrame
training_data.columns

# Rename columns to clean up the look 
renamed = training_data.rename(columns={
    "Character_in_show":"Character", 
    "Football_Shaped_Head":"Football Head", 
    "color_of_hair": "Hair Color"})
renamed.head()

# Organize columns into a more logical order
column_switch = renamed[["Character", "Football Head", "Hair Color", "Height"]]
column_switch.head()

# Not every CSV requires an encoding, but be aware this can come up
file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")

# Calculate the number of unique authors in the DataFrame
num_authors = books_df["authors"].nunique()
#OR
num_authors = len(books_df["authors"].unique())

#loc and iloc
# Grab the data contained within the "Berry" row and the "Phone Number" column
berry_phone = df.loc["Berry", "Phone Number"]
print("Using Loc: " + berry_phone)
also_berry_phone = df.iloc[1, 2]
print("Using Iloc: " + also_berry_phone)

# The following will select all rows for columns `first_name` and `Phone Number`
df.loc[:, ["first_name", "Phone Number"]].head()

#make a conditional statement, which will retrieve all data that the condition satisfies
#then throw it back into the dataframe
good_movie_easy = movie_short[movie_short["IMDB"] > 7]
good_movie_easy.head()
#OR
good_movies = movie_short.loc[movie_short["IMDB"] > 7, ["FILM", "IMDB", "IMDB_user_vote_count"]]
good_movies.head()

# Finally, export this file to an Excel spreadsheet -- without the DataFrame index.
unknown_movies.to_excel("output/movieWatchlist.xlsx", index=False)

#replace
df['Employer'] = df['Employer'].replace({
    'Not Employed': 'Unemployed'
    })
df['Employer'].value_counts()

# look for missing values
crime_df.count()

# drop null rows
new_variable = crime_df.dropna(how='any')
new_variable.head()
#another way is to add rows to variable if cell > 0

# Want to add up the seconds UFOs are seen? There is a problem
# Problem can be seen by examining datatypes within the DataFrame
usa_ufo_df.dtypes

# Using to_numeric() to convert a column's data into floats
usa_ufo_df["duration (seconds)"] = pd.to_numeric(
    usa_ufo_df["duration (seconds)"])
usa_ufo_df.dtypes

# Using GroupBy in order to separate the data into fields according to "state" values
grouped_usa_df = usa_ufo_df.groupby(['state'])
# The object returned is a "GroupBy" object and cannot be viewed normally...
print(grouped_usa_df)
# In order to be visualized, a data function must be used...
grouped_usa_df.count().head(10)

# Since "duration (seconds)" was converted to a numeric time, it can now be summed up per state
state_duration = grouped_usa_df["duration (seconds)"].sum()
state_duration.head()

# Creating a new DataFrame using both duration and count
state_summary_table = pd.DataFrame({"Number of Sightings": state_counts,
                                    "Total Visit Time": state_duration})
state_summary_table.head()

# It is also possible to group a DataFrame by multiple columns
# This returns an object with multiple indexes, however, which can be harder to deal with
grouped_international_data = clean_ufo_df.groupby(['country', 'state'])
# Converting a GroupBy object into a DataFrame
international_duration = pd.DataFrame(
    grouped_international_data["duration (seconds)"].sum())
international_duration.head(10)

# Bonus: Sort the table by strongest type and export the resulting table to a new CSV.
#ascending is the only one, there is no descending
strongest = pokemon_type_df.sort_values(["Total"], ascending = False)
strongest.reset_index(inplace = True) #inplace permanently saves the changes
strongest

# Sorting the DataFrame based on "Freedom" column
# Will sort from lowest to highest if no other parameter is passed
freedom_df = happiness_df.sort_values("Freedom")
freedom_df.head()

# To sort from highest to lowest, ascending=False must be passed in
freedom_df = happiness_df.sort_values("Freedom", ascending=False)
freedom_df.head()

# It is possible to sort based upon multiple columns
family_and_generosity = happiness_df.sort_values(
    ["Family", "Generosity"], ascending=False)
family_and_generosity.head()

# The index can be reset to provide index numbers based on the new rankings.
new_index = family_and_generosity.reset_index(drop=True)
new_index.head()

# Merge two dataframes using an inner join, their intersection
merge_table = pd.merge(info_pd, items_pd, on="customer_id")
merge_table

# Merge two dataframes using an outer join, both including things that don't intersect
merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="outer")
merge_table

# Merge two dataframes using a left join
merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="left")
merge_table

# Merge two dataframes using a right join
merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="right")
merge_table

# alternatively you can set your suffixes when the merge occurs
#replace the _x and _y for non-mergable columns
alt_merge = pd.merge(bitcoin_df, dash_df, on="Date", suffixes={" Bitcoin", " Dash"}) #include the space before bitcoin
alt_merge.head()

# Create the bins in which Data will be held
# Bins are 0-60, 61-70, 71-80, 81-90, 91-100
bins = [0, 60, 70, 80, 90, 100]
# Create the names for the four bins
group_names = ["F", "D", "C", "B", "A"]
#cut into original dataframe
df["Test Score Summary"] = pd.cut(df["Test Score"], bins, labels=group_names)
df

# Use Map to format all the columns
file_df["avg_cost"] = file_df["avg_cost"].map("${:.2f}".format) #2f is 2 floating points, rounds to 2 decimal places
file_df["population"] = file_df["population"].map("{:,}".format) #split numbers to use comma notation
file_df["percent"] = file_df["other"].map("{:.2f}%".format) #percent
file_df.head()