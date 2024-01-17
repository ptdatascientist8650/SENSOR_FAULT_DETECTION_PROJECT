import pymongo
import pandas as pd 
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH='/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME='aps'
COLLECTION_NAME='sensor'

if __name__=='__main__':
    df=pd.read_csv('/config/workspace/aps_failure_training_set1.csv')
    print(f'rows and columns:{df.shape}')
  # we have 36188 rows and 171 columns in our dataset.
  #convert data frame to json to dump records to mongodb 
    df.reset_index(drop=True,inplace=True)#to drop the index

    json_records=list(json.loads(df.T.to_json()).values())
    print(json_records[0])#0 for single record we have converted to json format 

    #insert converted json records to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)
    
    #connect with github repository to keep update there for maintaning across team 
    #copy url of that github repo with branch main 
    #delete origin (variable) first -remote (bcz it is not our)
    #check by=get git -v
    #delete = git remote remove origin 
    
    #lets connect by creating a varible=write git remote add origin then paste link 
    #first delete old git than create new git
    #by default there is some hidden git folder to see that folder write 
    #write cd .git/ cont...


    # to push write ---: git push origin main -f @check in github account whole things folders will be available there .)
    # -f means forcefully we made .






















