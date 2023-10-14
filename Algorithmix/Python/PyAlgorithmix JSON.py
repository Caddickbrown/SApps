#Import
import random, json, os

# Setup
input("\n" + "Hit Enter to Generate a New List")

# Loop
while (1 == 1):

    # Pull data and assign index numbers
    path=os.getcwd() # Define filepath
    with open(os.path.abspath(os.path.join(path, os.pardir))+"/list.JSON") as f:
    #with open(os.path.abspath(os.path.join(path, os.pardir))+"./list.JSON") as f:
        data = json.load(f)
        random_index_time = random.randint(0, len(data["timeunit"])-1)
        random_index_verb = random.randint(0, len(data["verbage"])-1)
        random_index_item = random.randint(0, len(data["item"])-1)
        random_index_emotion = random.randint(0, len(data["emotion"])-1)
        random_index_nounone = random.randint(0, len(data["nouns"])-1)
        random_index_nountwo = random.randint(0, len(data["nouns"])-1)

    # Generate words
    timeselect = data["timeunit"][random_index_time]
    verbselect = data["verbage"][random_index_verb]
    itemselect = data["item"][random_index_item]
    emotionselect = data["emotion"][random_index_emotion]
    nounselectone = data["nouns"][random_index_nounone]
    nounselecttwo = data["nouns"][random_index_nountwo]

    # Print
    print("\n" + "You have", random.randint(0,60), timeselect, "to", verbselect, itemselect + ". Your keywords are", nounselectone + ",", nounselecttwo + ", and", emotionselect + ". Good Luck!")
    input("\n" + "Hit Enter to Generate a New List")