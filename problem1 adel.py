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
projects_we_can_take = 0

for contributor in range(contributors):
    user, skills = f.readline().split(" ")
    skills = int(skills)
    user_dict[user] = {}
    user_dict[user]['skills'] = {}
    user_dict[user]['is_available'] = True
    user_dict[user]['days_left'] = 0
    for skill in range(skills):
        skill_name, skill_level = f.readline().split()
        skill_level = int(skill_level)
        user_dict[user]['skills'][skill_name] = skill_level

day = 0
while day < 100:
    
    day += 1

# Writing the submission file. Open the file
f = open("problem_a_output.txt", "w")
# First line is how many projects we can take
f.writeline(projects_we_can_take)
f.close()