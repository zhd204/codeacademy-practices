"""
This program generates passages that are generated in mad-lib format
Author: Katherin
"""

# The template for the story

# STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print "The Mad Libs has started!"

name = raw_input("Enter a name: ")

adj = list()
number_of_adj = 3
for i in range(number_of_adj):
    adj.append(raw_input("Enter an adjective:\n"))

verb = raw_input("Enter a verb:\n")

nouns = list()
number_of_nouns = 2
for i in range(number_of_nouns):
    nouns.append(raw_input("Enter a noun:\n"))

category_dict = {
    "animal": "",
    "food": "",
    "fruit": "",
    "superhero": "",
    "country": "",
    "desseret": "",
    "year": ""
}

for item in category_dict:
    category_dict[item] = raw_input("Enter an " + item + " :\n")

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." % (
name, adj[0], adj[1], category_dict['animal'], category_dict['food'], verb, nouns[0], category_dict['fruit'], adj[2],
name, category_dict['superhero'], name, category_dict['country'], name, category_dict['desseret'], name,
category_dict['year'], nouns[1])

print STORY
