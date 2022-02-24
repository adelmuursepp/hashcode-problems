f = open("input_data/a_an_example.in.txt", "r")

user_dict = {}

# Read the first line. First integer is number of contributors. Second is number of projects
# Save them as integers
first_line = f.readline().split(" ")
contributors = int(first_line[0])
projects = int(first_line[1])

for contributor in range(contributors):
    user, skills = f.readline().split(" ")
    skills = int(skills)
    user_dict[user] = {}
    for skill in range(skills):
        skill_name, skill_level = f.readline().split()
        skill_level = int(skill_level)
        user_dict[user][skill_name] = skill_level

print(user_dict)
