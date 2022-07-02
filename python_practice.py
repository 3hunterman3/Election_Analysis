'''
print("hello world")
'''

counties = ['Arapahoe','Denver','Jefferson']
if counties[1] == "Denver":
    print(counties[1])
'''
if counties[3] != 'Jefferson': #out of range so wont work will give an index error
    print(counties[2])
'''

temperature = int(input('what is the temperatue outside? '))

if temperature > 80:
    print('Turn on the AC.')
else:
    print('Open the windows.')

#what is the score?
score = int(input('what is your test score'))

#determine the grade
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C')
        else:
            if score >= 60:
                print('Your grade is a D')
            else:
                print('Your grade is an F')
