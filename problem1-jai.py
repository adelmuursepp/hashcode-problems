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
print(f"Projects: {project_skills}")
print(f"Skills: {skills}")

# Read the second line. First integer is number of projects. Second is number of skills
# Save them as integers
second_line = f.readline().split(" ")
projects = int(second_line[0])
skills = int(second_line[1])
print(f"Projects: {projects}")
print(f"Skills: {skills}")

# Create a dictionary for each project. The key is the project name and the value is a list of skills
project_dict = {}
for project in range(projects):
    project_name, skills = f.readline().split(" ")
    skills = int(skills)
    project_dict[project_name] = {}
    for skill in range(skills):
        skill_name, skill_level = f.readline().split()
        skill_level = int(skill_level)
        project_dict[project_name][skill_name] = skill_level

print(project_dict)

