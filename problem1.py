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

project_dict = {}

for project in range(projects):
    project_name, days_required, score_awarded, best_before, num_roles = f.readline().split(" ")
    days_required = int(days_required)
    score_awarded = int(score_awarded)
    best_before = int(best_before)
    num_roles = int(num_roles)
    project_dict[project_name] = {}
    project_dict[project_name]["days_required"] = days_required
    project_dict[project_name]["score_awarded"] = score_awarded
    project_dict[project_name]["best_before"] = best_before
    project_dict[project_name]["num_roles"] = num_roles
    project_dict[project_name]["roles"] = {}

    for role in range(num_roles):
        role_name, required_skills = f.readline().split(" ")
        required_skills = int(required_skills)
        project_dict[project_name]["roles"][role_name] = required_skills
<<<<<<< HEAD
i = 0
while i < 100:
    for project in project_dict:
        total_days = project["best_before"] + i 
        if total_days > project["best_before"]:
            points = project["score_awarded"] - (total_days - project["best_before"])
        
    i += 1 
print("Projects")
print(project_dict)
print(user_dict)
=======

day_tracker = 0


def is_day_available(user, day):
    if user['days_left'] == 0:
        return True
    days_till_day = day - day_tracker
    updated_days_left = user['days_left'] - days_till_day
    return updated_days_left <= 0
>>>>>>> 2c27318fe9e950db199cdf9abf1dd36720dc6cf7


def relative_skill(user, project):
    relative_skill_tracker = {}
    for skill in project['roles'].keys():
        if skill in user['skills'].keys():
            relative_skill_tracker[skill] = user['skills'][skill] - project['roles'][skill]
    return relative_skill_tracker


print(project_dict)
print(user_dict)
