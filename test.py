import sqlalchemy, json, requests, os, matplotlib
from sqlalchemy import create_engine 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'length': [1.5, 0.5, 1.2, 0.9, 3, 3],
    'width': [2.5, 0.5, 1.2, 0.9, 3, 3]
})

# create a method for visualization
def histogram(dataframe, column_name):
    dataframe.hist(column=column_name) # create the histogram
    plt.show()

def pullDataFromAPIintoPandasDF():
  col_names = ['Title', 'Author']
  dataframe  = pd.DataFrame(columns = col_names)
  
  response = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty")
  mostRecent = response.json()
  
  dataframe = getDataFromAPI(dataframe, mostRecent)
  
  print(dataframe)
  return dataframe
  
def getDataFromAPI(dataframe, mostRecent):
    id = mostRecent[0]
    story_url = "https://hacker-news.firebaseio.com/v0/item/"+str(id)+".json?print=pretty"
    json_file = requests.get(story_url).json()
    dataframe.loc[len(dataframe.index)] = [json_file["title"], json_file["by"]]
    return dataframe

def loadNewData(dataframe):
    dataframe.sort_values(by='Story_ID', inplace=True, ascending=False)
    neweststorysaved = dataframe.iloc[0,0]
    
    response = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty")
    mostRecent = response.json()
    
    dataframe = getDataFromAPI(dataframe, mostRecent)
    dataframe.sort_values(by='Story_ID', inplace=True, ascending=False)
    return dataframe
  
# Generalized method for migrating data     
 
def saveSQLtoFile(filename, database_name):
    os.system('mysqldump -u root -pcodio '+database_name+' > '+ filename)

def loadSQLfromFile(filename, database_name):
    #create database if it does not exist
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
    os.system("mysql -u root -pcodio "+database_name+" < " + filename)
  
def createEngine(database_name):
    return create_engine('mysql://root:codio@localhost/'+database_name+'?charset=utf8', encoding='utf-8')
    
def saveDatasetToFile(database_name, table_name, filename, dataframe):
    dataframe.to_sql(table_name, con=createEngine(database_name), if_exists='replace', index=False)
    saveSQLtoFile(filename, database_name)

def loadDataset(database_name, table_name, filename, update=False):
    loadSQLfromFile(filename, database_name)
    df = pd.read_sql_table(table_name, con=createEngine(database_name))
    if update:
        return loadNewData(df)
    else:
        return df

def add(a, b):
    return a + b
  
# Main function
if __name__ == "__main__":
    database_name = "articles"
    table_name = "new_stories"
    filename = "storylines.sql"
  
    #df = pullDataFromAPIintoPandasDF()
    #saveDatasetToFile(database_name, table_name, filename, df)
    
    #df = loadDataset(database_name, table_name, filename)
    #saveDatasetToFile(database_name, table_name, filename, df)
    
    #histogram(df, 'Width')
    
    