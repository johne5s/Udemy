with open('SchoolCodes.txt',mode='r') as my_new_file:
    contents = my_new_file.readlines()
    #print(contents)
    for line in contents:
        print(f'WHEN \'{line[0:5]}\' THEN \'{line[6:-2:]}\'')