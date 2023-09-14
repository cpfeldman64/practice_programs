# Make a list of some of my friends and loop through it with various messages


friends_list = ['austin', 'hope', 'ty', 'root', 'josh']

for friend in friends_list:
    if friend:
        print(f'Hi {friend}')

# a little weird, probably not the ideal method

print('\n\nend list\n\n')

friends_list.pop()

print(friends_list)

friends_list.append('josh')

print(friends_list)

favorite_dogs = {
    'austin': 'german shepherd',
    'hope': 'pitbull',
    'ty': 'pitbull',
    'root': 'corgi',
    'connor': 'doberman',
}

for key, value in favorite_dogs.items():
    print(f"\n{key.title()}'s favorite dog breed is the noble {value.title()}.")

favorite_dogs[key] = 'john'
favorite_dogs[value] = 'donkey'

print(favorite_dogs)
# whoo!

favorite_dogs.remove('john')

