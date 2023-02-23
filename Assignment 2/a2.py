# Assignment - 2
# Name - AMOLIKA BANSAL
# Roll No - 2020424

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	y=[]
	for i in records:
		if (i["first_name"].lower() ==first_name.lower()):
			y.append(i["id"])
	return y



def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	h = []
	for i in records:
		if (i["last_name"].lower()== last_name.lower()):
			h.append(i["id"])
	return h



def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	a = []
	# full_name=first_name.capitalize(),last_name.capitalize()
	m=full_name.split()
	x=m[0].lower()
	y=m[1].lower()
	hey=(x,y)
	for i in records:
		if (i["first_name"].lower(),i["last_name"].lower()) == hey:
			a.append(i["id"])
	return(a)


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	a = []
	for i in records:
		if (min_age<=i["age"]<=max_age):
			a.append(i["id"])
	return a


def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''

	males=0
	females=0
	for i in records:
		if (i["gender"] == "male"):
			males=males+1
		if (i["gender"] == "female"):
			females = females + 1
	a={"male":males, "female":females}
	return a



def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''



	q = True
	d_ids = list()
	for item in records:
		q = True
		for key in address.keys():
			if item['address'][key] != address[key]:
				if type(item['address'][key]) == str and type(address[key]) == str:
					if item['address'][key].casefold() != address[key].casefold():
						q = False
				else:
					q = False
		if (q == True):
			d_ids.append(item)

	filter_keys = ["first_name", "last_name"]
	filtered_dict = list()
	modified_dict = {}

	for x in d_ids:
		modified_dict = {key: value for key, value in x.items() if key in filter_keys}

		filtered_dict.append(modified_dict)
	return filtered_dict





def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
	h = []
	for i in records:
		for m in i["education"]:
			if m["ongoing"]==False:
				if institute_name==m["institute"]:
					h.append({"first_name":i["first_name"],"last_name":i["last_name"], "percentage":m["percentage"]})

	return h







def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
	s={}
	a=[]


	for i in records:
		for m in i["education"]:
			institute_name = m["institute"]
			a.append(institute_name)
	for u in a:
		topper=0
		n=0
		for i in records:

			for k in (i["education"][::-1]):
				if k["institute"]==u and k["ongoing"]==False:
					if k["percentage"] > topper:
						topper=k["percentage"]
						n=i["id"]
						break
		s[u]=n
						
	return s






def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	m={}
	for i in records:
		if i["id"]==receiver_person_id:
			blood_group=i["blood_group"]

	for j in records:
		if blood_group == "AB":
			if(j["id"]!=receiver_person_id):
				m[j["id"]]= j["contacts"]
		if blood_group == "A":
			if (j["id"] != receiver_person_id) and (j["blood_group"]=="A" or j["blood_group"]=="O"):
					m[j["id"]]=j["contacts"]
		if blood_group == "B":
			if (j["id"] != receiver_person_id) and (j["blood_group"]=="B" or j["blood_group"]=="O"):
					m[j["id"]]=j["contacts"]
		if blood_group == "O":
			if (j["id"] != receiver_person_id) and (j["blood_group"]=="O"):
					m[j["id"]]=j["contacts"]

	return m




def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''

	friend_list = []
	for x in list_of_ids:
		for y in records:
			if y['id'] == x:
				friend_list.append(y['friend_ids'])
			# print (friend_list)
	result = set(friend_list[0])
	for s in friend_list[1:]:
		result.intersection_update(s)

	return (list(result))








def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''

	return True



def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''


	for x in records:
		if x['id'] == person_id:
			records.remove(x)
		else:
			for y in x['friend_ids']:
				if y == person_id:
					x['friend_ids'].remove(y)

	return (records)




def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	for i in records:
		if person_id==i["id"]:
			if friend_id not in i["friend_ids"]:
				i["friend_ids"].append(friend_id)
	for f in records:
		if(friend_id)==f["id"]:
			if person_id not in i["friend_ids"]:
				f["friend_ids"].append(person_id)
	return (records)




def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	for x in records:
		if x['id'] == person_id:
			if friend_id in x["friend_ids"]:
				x['friend_ids'].remove(friend_id)

	for x in records:
		if x['id'] == friend_id:
			if person_id in x["friend_ids"]:
				x['friend_ids'].remove(person_id)
	return (records)



def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''


	di = dict(institute=institute_name, ongoing=ongoing, percentage=percentage)
	ip=  dict(institute=institute_name, ongoing=ongoing)
	for x in records:
		if x['id'] == person_id:
			if ongoing==True:
				x['education'].append(ip)
			else:
				x['education'].append(di)


	return (records)




