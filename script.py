import requests, json
import pandas as pd

query = {'find': 'allsms'}


data = requests.post('https://enigmatic-woodland-58661.herokuapp.com/statistics', json = query).json()

    
string_dict = data['response']

data_json = json.loads(string_dict)

data_df = pd.DataFrame(data_json)

values = data_df['street_name'].value_counts()


#----getting the issue which occur in great extend--------------------

# max_number_of_issues = data_df['street_name'].value_counts().max()
# print(max_number_of_issues)
# #print(data_df)
# #print(values)

def get_area_with_max_issue_by_number(data_df):
    max_number_of_issues = data_df['street_name'].value_counts().max()
    area_max = print(max_number_of_issues)
    return area_max

get_area_with_max_issue_by_number(data_df)
print('should be a number')



#----------------------------------------------------------------------------------------------------
# we use df.series.mode() to get the name of the data entry that has the highest number of  occurance
# let create a function to get the name of the entry

#----------------------------------------------------------------------------------------------------

#function of the name
# def get_most_affected():

#     area_most_affected = data_df.street_name.mode()
#     return area_most_affected
print(data_df.mode)
print('should be a name')
#------------------------------------------------------------------------------------------------------
# get the total number of sms with following f(x)

#------------------------------------------------------------------------------------------------------

def get_total_sms():
    total_number_of_sms = len(data_df)
    total = print(total_number_of_sms)
    return total
get_total_sms()


#------------------------------------------------------------------------------------------------------
# Getting the number  of users who are using this service
# we get this number by querying from the the database

#query action is query


#------------------------------------------------------------------------------------------------------


def get_stats_to_panel():
    total_sms = get_total_sms()
    #most_affected = get_most_affected()
    most_affected_in_number = get_area_with_max_issue_by_number(data_df)

    return total_sms, most_affected_in_number

get_stats_to_panel()

print(data_df.info())