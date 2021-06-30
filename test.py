import sqlalchemy, json, requests
from sqlalchemy import create_engine
import pandas as pd

# Retreives id numbers of newstories and converts into json 
# Testing 1: Make sure API is working, if 200 shows up-> works, else-> broken
# Testing 2: Make sure the url isnt empty, if empty, return error statment
# Testing 3: Make sure the return value is a list (Output should be list of values)
def convert_to_json(url):
    r = requests.get(url).json()
    return r

# Grabs the first index in the json and creates the url link to the new story
# Testing 1: Check if 'id' is a number
# Testing 2: Check if url works, if null-> doesn't work
# Testing 3: 
def specifc_new_story_url(response):
    id = response[0]
    story_url = "https://hacker-news.firebaseio.com/v0/item/"+str(id)+".json?print=pretty"
    return story_url
  
# Converts the new story information to a json
# Testing 1: Make sure the info (Title, author) you want is in the json file 
# Testing 2: Make sure return value so dict., else create error statment
# Testing 3: 
def new_url_to_json(url):
  response = requests.get(url).json()
  return response

# Creates a table and returns DataFrame
# Testing 1: Check if the values or null, if so return NONE
# Testing 2: 
def create_table(json_file):
    col_names = ['Title', 'Author']
    df = pd.DataFrame(columns = col_names)
    df.loc[len(df.index)] = [json_file["title"], json_file["by"]]
    return df

# Exports dataframe to mysql
# Testing 1: Check if database is created
# Testing 2: 
def export_to_mysql(df):
    engine = create_engine('mysql://root:codio@localhost/test')
    df.to_sql('test', con=engine, if_exists='replace', index=False)

# Main function
if __name__ == "__main__":
    # API link to number of newstories
    url = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
    
    json_file = convert_to_json(url)
    new_story_url = specifc_new_story_url(json_file)
    new_story_json_file = new_url_to_json(new_story_url)
    data_frame = create_table(new_story_json_file)
    export_to_mysql(data_frame)