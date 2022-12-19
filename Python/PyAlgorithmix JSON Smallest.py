#Import
import random, json, os

# Setup
input("\n" + "Hit Enter to Generate a New List")

# Loop
while (1 == 1):

    # Pull data
    path = os.getcwd() # Define filepath
    data = json.load(open(os.path.abspath(os.path.join(path, os.pardir))+"/list.JSON"))

    # Generate words
    timeselect = data["timeunit"][random.randint(0, len(data["timeunit"])-1)]
    verbselect = data["verbage"][random.randint(0, len(data["verbage"])-1)]
    itemselect = data["item"][random.randint(0, len(data["item"])-1)]
    emotionselect = data["emotion"][random.randint(0, len(data["emotion"])-1)]
    nounselectone = data["nouns"][random.randint(0, len(data["nouns"])-1)]
    nounselecttwo = data["nouns"][random.randint(0, len(data["nouns"])-1)]

    # Print
    print("\n" + "You have", random.randint(0,60), timeselect, "to", verbselect, itemselect + ". Your keywords are", nounselectone + ",", nounselecttwo + ", and", emotionselect + ". Good Luck!")
    input("\n" + "Hit Enter to Generate a New List")