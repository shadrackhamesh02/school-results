#Nested if condition

print('School Records')
name = input('Enter Name: ')
std = input('Enter Standard: ')
team1 = int(input('Enter Team 1 Marks: '))
team2 = int(input('Enter Team 2 Marks : '))
team3 = int(input('Enter Team 3 Marks : '))
total = team1 + team2 + team3
avg = total / 3
print('...............-Student Details-...............')
print('Name               : ', name)
print('Standard           : ', std)
print('Teams              : ', team1, ' - ', team2, ' - ', team3)
print('Total              : ', total)
print('Average            :', avg)

# Validate Result

if team1 >= 452 and team2 >= 422 and team3 >= 359:

    print('Result : PASS')

    if avg > 450 and avg <= 500:

        print('Grade: Grade A')

    elif avg > 400 and avg <= 450:

        print('Grade : Grade B')

    elif avg > 350 and avg <= 400:

        print('Grade : Grade C')

    else:

        print('Grade : Grade D')

else:

    print('Result : FAIL')

    print('Grade : U ')

print('Pass means Good luck Otherwise Better Luck Next Time.')