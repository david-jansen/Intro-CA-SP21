"""
This is a sample Python script called encouragement_bot.py. It will print out
a message of encouragement based on a user's preference. You can run it by
typing `python encouragement_bot.py` on the command line. Feel free to use
as a model for your own scripts.
"""

encouragement = "You're doing amazing, sweetie"

print("Please enter your preferred delivery mode of encouragement. Type 'loud' or 'gentle':")
preference = input()


if preference == 'loud':
    print(encouragement.upper())
elif preference == 'gentle':
    print(encouragement.lower())
else:
    print("Delivery mode not recognized — sorry try again (but you're still doing amazing!")