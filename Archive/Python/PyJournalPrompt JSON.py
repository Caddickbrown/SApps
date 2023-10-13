#Import
import random, json, os, time

# Setup
input("Hit Enter to Generate a New Prompt")

# Loop
while (1 == 1):

    # Pull data and assign index numbers
    path=os.getcwd() # Define filepath
    with open(os.path.abspath(os.path.join(path, os.pardir))+"./list.JSON", encoding="utf8") as f:
        data = json.load(f)
        #time.sleep(100000)
        random_index_prompt = random.randint(0, len(data["prompt"])-1)

    # Generate words
    promptselect = data["prompt"][random_index_prompt]

    # Print
    print("\n\t" + promptselect)
    
    input("\n" + "Hit Enter to Generate a New Prompt")


# Additional complexity could be added with "try and write 100 words about it" or something - but randomise the number