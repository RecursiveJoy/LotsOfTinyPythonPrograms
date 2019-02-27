def main():
    #create two lists

    names = ['Michael', 'Gob', 'Buster', 'Maybe', 'Lucille', 'Lindsay', 'Marta', \
             'George', 'Annyong', 'Tobias']
    numbers = ['555-4011','555-9865', '555-5755', '555-3161', '555-0022', \
               '555-4651','555-0605', '555-1115', '555-3061', '555-7017']

    #prompt user for a name

    name = input('Enter the name of the person whose phone number you want: ')

    #get index of the name in the name list

    index = names.index(name)

    #print the value of the phone number with that same index

    print(numbers[index])

main()
