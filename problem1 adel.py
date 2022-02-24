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

i = 0
for i in range(100):
    for project in project_dict:
        # print(project)
        total_days = int(project_dict[project]["best_before"]) + i 
        if total_days > int(project_dict[project]["best_before"]):
            points = int(project_dict[project]["score_awarded"]) - (total_days - int(project_dict[project]["best_before"]))
        users_available = []
        for user in user_dict:
            if is_day_available(user, i):
                users_available.append(user)
        skills = project_dict[project]["roles"]
        users_with_rel_skills = {}
        for user in users_available:
            relative_score = relative_skill(user_dict[user], project_dict[project])
            if relative_score == {}:
                pass
            else:
                for relative_skill in relative_score:
                    if relative_score[relative_skill] >= -1:
                        users_with_rel_skills[user] = relative_score[relative_skill]
                    else:
                        pass

# Writing the submission file. Open the file
f = open("problem_a_output.txt", "w")
# First line is how many projects we can take
f.writeline(projects_we_can_take)
f.close()