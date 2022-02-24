import os

# code which gets the absolute path of the input_data directory
dir_path = os.path.dirname(os.path.realpath(__file__))
input_data_path = os.path.join(dir_path, 'input_data')
f = open(f'{input_data_path}\\a_an_example.in.txt', "r")


# Read the second line. First integer is number of projects. Second is number of skills
# Save them as integers
second_line = f.readline().split(" ")
project_skills = int(second_line[0])
skills = int(second_line[1])
