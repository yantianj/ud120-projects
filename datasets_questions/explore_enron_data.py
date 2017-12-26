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
# print(enron_data.keys())    

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

### whose total_payments is largest among Jeffrey Skilling,Kenneth Lay:max,Andrew Fastow
print (enron_data["SKILLING JEFFREY K"]["total_payments"])    # enron CEO : Jeffrey Skilling : 8682716
print (enron_data["LAY KENNETH L"]["total_payments"])    # enron chairman : Kenneth Lay : 103559793
print (enron_data["FASTOW ANDREW S"]["total_payments"])    # enron CFO : Andrew Fastow : 2424083

### all the features of one person
# print(enron_data["METTS MARK"])

### the number of folks in this dataset have a quantified salary number and know email address.
person_quantified_salary = 0
email_address = 0
person_name = enron_data.keys()
for num in range(len(person_name)):
	if type(enron_data[person_name[num]]['salary'] ) == int :
		person_quantified_salary = person_quantified_salary + 1
	if enron_data[person_name[num]]['email_address'] != "NaN" :
		email_address = email_address + 1
print ("the number of people who have a quantified salary number : %d"  % person_quantified_salary)
print ("the number of people who have email address : %d"  % email_address)

### the sum of peoples'total_payments equals to 'NaN' and their percentage in the whole dataset.
number_total_payments = 0
person_name = enron_data.keys()
total_person_number = len(person_name)
print ("total_person_number : %d"  % total_person_number)
for num in range(len(person_name)):
	if enron_data[person_name[num]]['total_payments'] == "NaN" :
		number_total_payments = number_total_payments + 1
print ("the number of people who have not been known total_payments : %d"  % number_total_payments)
print ("percentage in the whole dataset : %d " % (number_total_payments*100/total_person_number))
# format(float(number_total_payments)/float(total_person_number),'.5f')

### the sum of POI'total_payments equals to 'NaN' and their percentage in the whole POI dataset.
person_poi = 0
number_nan_poi = 0
person_name = enron_data.keys()
for num in range(len(person_name)):
	if enron_data[person_name[num]]['poi'] == 1 :
		person_poi = person_poi+1
		if enron_data[person_name[num]]['total_payments'] == "NaN" :
			number_nan_poi = number_nan_poi + 1	
print ("percentage in the whole POI dataset : %d " % (number_nan_poi*100/person_poi))
print (number_nan_poi, person_poi )

