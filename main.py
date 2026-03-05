print("Hey guy!\n")
print("Let's play a ittle game.\nYou give me words, and I'll give you a story.\nReally fun stuff, i promise!\n")
print("""Now, I have three stories you can play with\(unfortunately none of them include Shrek) """)

# story one

def harrheal():
    print("Great choice! just fill out the following to start!")
    num1= input("Let's start with a number: ")
    time1= input("And now, a measure of time\(like years, decades etc.):")
    trns1= input ("What would be your preferred vehicle to get to a hospital in? ")
    adj1= input("Now I'll need an adjective: ")
    adj2= input("And another one: ")
    noun1= input("I'll need a noun now: ")
    color1= input("What is your favourite color? ")
    body_part1=input("Head to toe, name a body part, GO! ")
    verb1= input ("Think of a verb, now type it out: ")
    num2= input("Hmmmm... Looks like i'm gonna need another number now: ")
    noun2= input("Noun")
    noun3=input ("Another noun")
    body_part2=input("body part")
    print("\nOkay I'm getting tired, lemme take a little sip of my white monster.\n")
    verb2=("Okay I'm good again, sooooo good!!! I'll need another verb from you: ")
    noun4=("Almost done , give me a noun: ")
    adj3= ("And and adjective: ")
    silly_word=("And a silly word")
    return f" It was about {num1} {time1} ago when I arrived at the hospital in a {trns1}.\n The hospital is a/an {adj1} place, there are a lot of {adj2} {noun1} here.\n There are nurses here who have {color1} {body_part1}.\n If someone wants to come into my room I told them that they have to {verb1} first.\n I’ve decorated my room with {num2} {noun2}.\n Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}.\n I heard that all doctors {verb2} {noun3} every day for breakfast.\n The most {adj3} thing about being in the hospital is the {silly_word} {noun4} ! "


def camcar():
    print("Aweseome choice!\nDefinitely my favourite")
    name1= input("Give me a name, any name, werid name even: ")
    noun1=input("And a noun: ")
    adj1= input("Name a feeling: ")
    verb1=input("We'll need a verb now: ")
    adj2= input("Another feeling please: ")
    animal1=input("What animal do you fear the most? ")
    verb2=input("What is the first verb that comes to your mind? ")
    color1=input("Look straight in front of you, what is the first color that you see? ")
    verb3=input("So many verbs, think of the possibilities!\(gotta end in -ing tho) ")
    adv= input("Think of something ending in -ly\(happily, sadly, hopefully, etc.)")
    num1=input("Enter a number: ")
    time1=input("We need a measure of time\(think minutes and hours)")
    color2=input("Enter a color: ")
    animal2=input("What animal do you find the cutest?")
    num2=input("Enter a number: ")
    silly_word=("A silly word: ")
    noun2=("And the last thing we need in a noun :D\n")
    return f" This weekend I am going camping with {name1}.\n I packed my lantern, sleeping bag, and {noun1}.\n I am so {adj1} to {verb1} in a tent.\n I am {adj2} we might see a/an {animal1}, I hear they\’re kind of dangerous.\n While we\’re camping, we are going to hike, fish, and {verb2}.\n I have heard that the {color1} lake is great for {verb3}. Then we will {adv} hike through the forest for {num1} {time1}.\n If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet!\n At night we will tell {num2} {silly_word} stories and roast {noun2} around the campfire!!"

def penpal():
    print("Ooooh heck yeah, mystical stuff!")
    name1= input("So, What's your mysterious pen pal's name? ")
    adj1=input("Now let's set up the story, we need an adjective: ")
    color1=input("What color shirt are you wearing? ")
    animal1=input("What animal would fit your mystical story best? ")
    place1=input("Name a place: ")
    adj2= input("Give me an adjective: ")
    mgc_creature1=input("Magical creatures are cool right? Name one then(plural): ")
    adj3=input("I want an adjective: ")
    mgc_creature2=input("Since you like magical creatures so much, name another one.(plural again) ")
    room=input("Which room of a  house comes to your mind? ")
    noun1=input("I'll need a noun now: ")
    noun2=input("Sike, I needed two nouns, give me another one: ")
    noun3= input("Sike again! I actually needed three nouns, this one need to be plural tho ")
    adj4=input("See, we're done with nouns now. i need an adjective now: ")
    noun4=input("MORE PLURAL NOUNS, THE FOREST CALLS FOR THEM! ")
    num1=input("the forest wants numbers too, apparently: ")
    time=input("Name a measure of time: ")
    verb=input("And now, a verb ending in -ing: ")
    adj5=input("Another adjective please: ")
    noun5= input("This is the last noun, i promise, and since I'm such a nice guy i don't need plurals;D \n")
    return f" Dear {name1}, I am writing to you from a/an {adj1} castle in an enchanted forest.\n I found myself here one day after going for a ride on a {color1} {animal1} in {place1}.\n There are {adj2} {mgc_creature1} and {adj3} {mgc_creature2} here!\n In the {room} there is a pool full of {noun1}.\n I fall asleep each night on a {noun2} of {noun3} and dream of {adj4} {noun4} It feels as though I have lived here for {num1} {time}.\n I hope one day you can visit, although the only way to get here now is {verb} on a {adj5} {noun5}!!"

def start_game():
    stories = {
        "1": harrheal,
        "2": camcar,
        "3": penpal,
    }

    while True:
        print("\nWhich story would you like to play with? ")
        print("1 - Harrowing Healthcare")
        print("2 - Camping Carnage")
        print("3 - Pen Pal")

        choice = input("Enter 1, 2 or 3: ")

        if choice not in stories:
            print("Invalid choice. Please try again.")
            continue

        print("\nYour story is done!\n")
        story_text = stories[choice]()
        print(story_text)

        # play again?
        while True:
            again = input("\nThat was fun right? Do you want to try another one?\(yes/no) ").lower()
            if again in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        if again == "no":
            print("\n Hey well, thank you spending time with me , I'm here if you ever want to come visit for some more stories!\n \n Byeeeeeeeeeeeeeeee!!!!!!!!!!!!")
            break


start_game()
