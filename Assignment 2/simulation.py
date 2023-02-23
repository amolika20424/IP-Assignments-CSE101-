# Name - Amolika Bansal
# Roll No - 2020424



'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.

'''

import a2

def greet():
    print("Hello! hope you're having a good day :)")
greet()
print()
def menu():
    print("Here is a drop down menu for your referance, please check the code number for which you have a query. ")
    print()
    print('''1. read_data_from_file 
2. filter_by_first_name
3. filter_by_last_name
4. filter_by_full_name
5. filter_by_age_range
6. count_by_gender
7. filter_by_address
8. find_alumni
9. find_topper_of_each_institute
10. find_blood_donors
11. get_common_friends
12. is_related
13. delete_by_id
14. add_friend
15. remove_friend
16. add_education''')
menu()



print()


def main():
    records=a2.read_data_from_file()

    # s = int(input("Please enter your query number (please enter -1 if you have no query or your query has been resolved: "))

    # if(s==-1):
    #     print("thank you, have a good day!")
    # elif (1<=s<=16):
    while True:
        s = int(input("Please enter your query number (please enter -1 if you have no query or your query has been resolved: "))

        if s==-1:
            print("thank you, have a good day!")
            break
        elif (s in range(1,17))==False:
            print("please enter a valid input from the options given")
        else:
            l = a2.read_data_from_file()
            if s==1:
                print(records)

            elif s==2:
                first_name = str(input("Enter first name: "))
                print(a2.filter_by_first_name(l, first_name))
                # print(y)
            elif s==3:
                last_name = str(input("Enter last name: "))
                print(a2.filter_by_last_name(l, last_name))
                # print(h)
            elif s==4:
                full_name = str(input("Enter full name: "))
                print(a2.filter_by_full_name(l, full_name))

            elif s==5:
                min_age = int(input("Enter min age: "))
                max_age = int(input("Enter max age: "))
                print(a2.filter_by_age_range(l, min_age, max_age))

            elif s==6:
                print(a2.count_by_gender(l))
            elif s==7:
                dicti={}
                house_no=(input("enter house no: "))
                block=(input("enter block name: "))
                town= str(input("enter town name: "))
                city=str(input("enter city name: "))
                state=str(input("enter state name: "))
                pincode=(input("enter pincode number: "))
                if len(house_no) != 0:
                    dicti['house_no'] = int(house_no)
                if len(block) != 0:
                    dicti['block'] = block.upper()
                if len(town) !=0:
                    dicti['town'] = town
                if len(city) != 0:
                    dicti['city'] = city
                if len(state) != 0:
                    dicti['state'] = state
                if len(pincode) != 0:
                    dicti['pincode'] = int(pincode)

                print(dicti)
                print(a2.filter_by_address(l, dicti))

            elif s==8:
                institute_name = str(input("Enter institute name: "))
                print(a2.find_alumni(l, institute_name))

            elif s==9:
                print(a2.find_topper_of_each_institute(l))

            elif s==10:
                receiver_person_id = int(input("enter ID: "))
                print(a2.find_blood_donors(l, receiver_person_id))

            elif s==11:
                list_of_ids = list(map(int, input("Enter space seperated inputs: ").split()))
                print(a2.get_common_friends(records, list_of_ids))


            elif s==12:
                print("hey please, not this one")
            elif s==13:
                person_id = int(input("Enter personal id: "))
                records=(a2.delete_by_id(records, person_id))
                print(records)
                print("id has been deleted")

            elif s==14:
                person_id = int(input("Enter personal id: "))
                friend_id = int(input("Enter friend id: "))
                records=(a2.add_friend(records, person_id, friend_id))
                print(records)
                print("friend has been added")

            elif s==15:
                person_id = int(input("Enter personal id: "))
                friend_id = int(input("Enter friend id: "))
                records=(a2.remove_friend(records, person_id, friend_id))
                print(records)
                print("friend has been removed")

            elif s==16:
                person_id = int(input("Enter personal id: "))
                institute_name=str(input("enter institute name: "))
                ongoing=str(input("enter True or False: "))

                if ongoing=='False':
                    percentage=float(input("Enter percentage: "))
                    records = (a2.add_education(records, person_id, institute_name, ongoing, percentage))
                    print(records)
                    print("education has been added")
                else:
                    percentage=0
                    records=(a2.add_education(records, person_id, institute_name , ongoing, percentage))
                    print(records)
                    print("education has been added")


if __name__=="__main__":
    main()





















