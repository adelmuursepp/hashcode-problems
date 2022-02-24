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
        
print("Projects")
print(project_dict)
print(user_dict)


