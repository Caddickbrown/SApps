#Import
import random, json, os

# Setup
input("\n" + "Hit Enter to Generate a New List")

# Loop
while (1 == 1):

    # Pull data
    data = json.load(open(os.os.getcwd().abspath(os.os.getcwd().join(os.getcwd(), os.pardir))+"/list.JSON"))

    # Print
    print("\n" + "You have", random.randint(0,60), data["timeunit"][random.randint(0, len(data["timeunit"])-1)], "to", data["verbage"][random.randint(0, len(data["verbage"])-1)], data["item"][random.randint(0, len(data["item"])-1)] + ". Your keywords are", data["nouns"][random.randint(0, len(data["nouns"])-1)] + ",", data["nouns"][random.randint(0, len(data["nouns"])-1)] + ", and", data["emotion"][random.randint(0, len(data["emotion"])-1)] + ". Good Luck!")
    input("\n" + "Hit Enter to Generate a New List")