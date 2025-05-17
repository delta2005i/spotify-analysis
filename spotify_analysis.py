import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\\laksh\\Downloads\\spotify.csv')

#extracting the release year from the release date 
def chk(x):
    if len(x) < 5:
        return x
    else:
        return x.split('-')[2]  

df['release_year'] = df['release_date'].apply(chk)

#deleting the columns which are not in use 
df.drop('release_date',axis=1,inplace=True)
df.drop('id',axis=1,inplace=True)
df.drop('spotify_url',axis=1,inplace=True)

#changing the datatype of release year column to integer
df['release_year']=df['release_year'].astype('int64')

#popular song of every year
df.loc[df.groupby('release_year')['popularity'].idxmax()].set_index('release_year')['track_name']

#popular artist of every year 
df.loc[df.groupby('release_year')['popularity'].idxmax()].set_index('release_year')['artist']

#top 10 consistent popular artist
df.groupby('artist')['popularity'].mean().sort_values(ascending=False).head(10)

#top 10 most popular albums 
df.groupby('album')['popularity'].mean().sort_values(ascending=False)

#most popular album of every year
df.groupby(['release_year', 'album'])['popularity'].mean().groupby(level=0).apply(lambda x:x.idxmax()).str.get(1)

#average song length of every artist
df.groupby('artist')['duration_min'].mean()

#popularity and duration coorelation
print(df['popularity'].corr(df['duration_min']))

