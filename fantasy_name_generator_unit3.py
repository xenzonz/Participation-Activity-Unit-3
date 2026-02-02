""" 
Docstring for Participation Activity Unit 3 
i. Fantasy Name Generator
ii. Sam Cocquyt
iii. Generate random elf names
iv. No starter code
v. 2/1/2026
"""

import random

# first name syllables, elf like
first_beginning = ["Ae", "Eli", "Fa", "Lia", "Syl"]
first_middle    = ["ri", "la", "sha", "the", "nys"]
first_ending    = ["wyn", "riel", "thir", "loth", "diel"]

# last name words, elf like
last_beginning = ["Moon", "Star", "Silver", "Dawn", "Night"]
last_ending    = ["whisper", "bloom", "runner", "song", "glade"]

# first name generator function
def generate_first_name():
    first_name = random.choice(first_beginning) + random.choice(first_middle) + random.choice(first_ending)
    return first_name

# last name generator function
def generate_last_name():
    last_name = random.choice(last_beginning) + random.choice(last_ending)
    return last_name

# combine functions
def combine_generated_names():
    return generate_first_name() + " " + generate_last_name()

# for loop to generate a number of names
for _ in range(10):
    print(combine_generated_names())



