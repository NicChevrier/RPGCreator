import random
import names
import statistics

# Define the list of races, classes, and skills
races = ["Human", "Elf", "Dwarf"]
classes = ["Warrior", "Mage", "Thief", "Cleric", "Ranger"]
skills = ["Combat", "Scouting", "Mechanics", "Persuasion", "Stealth", "Healing", "Archery", "Crafting", "Survival", "Intimidation"]

# Choose a random race and class for the character
race = random.choice(races)
char_class = random.choice(classes)

# Generate a random set of skills for the character
skills = {skill: random.uniform(1, 10) for skill in skills}

# Generate a random first and last name for the character
first_name = names.get_first_name()
last_name = names.get_last_name()

# Calculate the average skill score for the character
average_skill_score = statistics.mean(skills.values())

# Ensure that the average skill score is normally distributed
mean = 5
stdev = 2
average_skill_score = random.normalvariate(mean, stdev)

# Print the character's information
print(f"Name: {first_name} {last_name}")
print(f"Race: {race}")
print(f"Class: {char_class}")
print("Skills:")
for skill, score in skills.items():
    print(f"  {skill}: {score:.1f}")
print(f"Average Skill Score: {average_skill_score:.1f}")
