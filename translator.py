def add_words():
    adding_words = True
    while adding_words:
        word=input("Enter english: ")
        translation=input("Enter german: ")
        english_to_german[word.lower().strip()]=translation.strip()
        print(f"\n'{word}' successfully added to the translator!")
        valid_input=False
        while not valid_input:
            more_words=input("Would you like to add another word (y/n)? ")
            if more_words == "n":
                print("Returning to translator...\n")
                adding_words=False
                valid_input=True
            elif more_words == "y":
                valid_input=True
            else:
                print("I'm sorry, I didn't catch that - please enter y/n")


english_to_german_dict = {
    "one": "eins",
    "two":"zwei",
    "three": "drei",
    "four": "vier",
    "five": "fünf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten":"zehn"
}

print("Welcome to the English-German Translator!\n\nHow to use:\n• Enter a word to translate to german\n• type 's' to switch translation direction\n• type 'a' to add a word\n• type 'q' to quit\n")

english_to_german=True
running = True

while running:
    action_done=False
    word = input("Enter word to translate: ")
    if word.lower() == "a":
        add_words()
        action_done=True

    elif word.lower() == "s":
        english_to_german=not english_to_german
        print("Switching translation direction...\n")
        action_done=True

    elif word.lower() == "q":
        running = False
        action_done=True

    elif english_to_german:
        if word.lower() in english_to_german_dict.keys():
            print(f"{word.lower()}: {english_to_german_dict[word.lower()]}\n")
            action_done=True

    elif not english_to_german:
        for english,german in english_to_german_dict.items():
            if word.lower() == german.lower():
                print(f"{german}: {english}\n")
                action_done=True

    if not action_done:
        print(f"Unfortunately, '{word.lower()}' isn't in my vocabulary.\n")

print("\nThank you for using the English to German Translator. Goodbye!")
