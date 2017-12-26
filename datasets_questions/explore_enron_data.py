#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

""" enron_data :Two-dimensional dictionary 
enron_data_1d is name of each person,enron_data_2d is features of each person"""

### length of enron_data_1d and name of each person
print(len(enron_data))    
print(enron_data.keys())    

### length of enron_data_2d and features of each person
print(len(enron_data["METTS MARK"])) 
print(enron_data["METTS MARK"].keys())

### "POI"(Person of interest):the number of POI==1 in enron_data.
person_poi = 0
person_name = enron_data.keys()
for num in range(len(person_name)):
	if enron_data[person_name[num]]['poi'] == 1 :
		person_poi = person_poi+1
print (person_poi)
		
###practice: 
print("the total value of the stock belonging to James Prentice is %d" % (enron_data["PRENTICE JAMES"]["total_stock_value"]))
print("the number of emails from_this_person_to_poi is %d" % (enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]))
print("the value of exercised_stock_options belonging to Jeffrey Skilling is %d" % (enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]))

