# write your code here
#1
person = {
    'name': 'Ahmed',
    'age': '21',
    'hobbies': {'Biking', 'Running'}
}

#print(person['name'])
#print(person['age'])

#2
person['age']=22
person['country'] = 'Kuwait'
#print(person)
person_dictionary = person.keys()
print(person_dictionary)


#3

person['hobbies'] = "Swimming",'Biking', 'Running', "Sleeping"
print(person['hobbies'])

def check_hobbies(person):
    if len(person['hobbies']) > 3 :
        print("Wow youre amazing")

check_hobbies(person)
#print(check_hobbies)