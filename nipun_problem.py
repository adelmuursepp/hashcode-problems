import os

# code which gets the absolute path of the input_data directory
dir_path = os.path.dirname(os.path.realpath(__file__))
input_data_path = os.path.join(dir_path, 'input_data')
f = open(f'{input_data_path}\\a_an_example.in.txt', "r")

user_dict = {}

# Read the first line. First integer is number of contributors. Second is number of projects
# Save them as integers
first_line = f.readline().split(" ")
contributors = int(first_line[0])
projects = int(first_line[1])

