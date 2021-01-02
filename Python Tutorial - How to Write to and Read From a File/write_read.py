path = r'' # e.g. C:\Users\Fabio-Work\Desktop\python_project\my_file.txt
text_to_write = input('Enter some text --> ')
text_to_write += '\n'

# try:
#     opened_file = open(path, 'w')
#     opened_file.write(text_to_write)
# except:
#     print('An error occured')
# finally:
#     opened_file.close()

# try:
#     opened_file = open(path, 'r')
#     content = opened_file.read()
# except:
#     print('An error occured')
# finally:
#     opened_file.close()

# print(content)

with open(path, 'a') as opened_file:
    opened_file.write(text_to_write)

# with open(path, 'r') as opened_file:
#     content = opened_file.read()
#     print(content)

with open(path, 'r') as opened_file:
    for line in opened_file:
        print(line, end='')
