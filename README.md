# PRIMM Lesson: Python Dictionaries

## Learning Objectives
By the end of this lesson, you will be able to:
- Understand what dictionaries are and how they store key-value pairs
- Create and access dictionary data
- See how dictionaries can replace multiple if/else statements
- Apply dictionary concepts to improve existing code

## PREDICT 🔮

Look at this code and predict what will be printed:

```python
student_grades = {
    "Elara": 85,
    "Kwame": 92,
    "Siobhan": 78,
    "Kai": 96
}

print(student_grades["Kwame"])
print(student_grades.get("Aisha", "Not found"))

result = student_grades["Elara"]
print(result)

print(student_grades["Aisha"])

# What do you think each print statement will output?
```

## RUN ⚡

Run the code in `predict.py` and see if you were right.

Now try these experiments:

```python
# Experiment 1: Adding new data
student_grades["Rory"] = 88
print(student_grades)

# Experiment 2: What happens with missing keys?
print(student_grades["Liam"])  # What error do you expect?
```

**Observations:**
- What happened when you added Rory?
- What error occurred with Liam?
- How is `.get()` different from using square brackets `[]`?

## INVESTIGATE 🔍

### What are Dictionaries?

Dictionaries store data as key-value pairs. Think of them like a real dictionary where you look up a word (key) to find its definition (value).

```python
# Dictionary structure
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

### Common Dictionary Operations

```python
# Creating dictionaries
colours = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

# Accessing values
print(colours["red"])        # Direct access
print(colours.get("red"))    # Safe access

# Adding/updating
colours["yellow"] = "#FFFF00"
colours["red"] = "#CC0000"   # Updates existing key

# Checking if key exists
if "purple" in colours:
    print("Purple exists!")

# Getting all keys or values
print(colours.keys())    # All keys
print(colours.values())  # All values
```

### Investigation Tasks:

1. Create a dictionary called `favourite_foods` with at least 4 people's names as keys and their favourite foods as values.

2. Write code to:
   - Add a new person
   - Change someone's favourite food
   - Safely check for someone who might not be in the dictionary

3. Compare these two approaches for handling user choices:

**Approach A (Multiple if/else):**
```python
user_choice = input("Pick a colour: ")

if user_choice == "red":
    hex_code = "#FF0000"
elif user_choice == "green":
    hex_code = "#00FF00"
elif user_choice == "blue":
    hex_code = "#0000FF"
else:
    hex_code = "Unknown colour"

print(f"Hex code: {hex_code}")
```

**Approach B (Dictionary):**
```python
colour_codes = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}

user_choice = input("Pick a colour: ")
hex_code = colour_codes.get(user_choice, "Unknown colour")
print(f"Hex code: {hex_code}")
```

**Questions:**
- Which approach is shorter?
- Which would be easier to add 10 more colours to?
- Which is easier to read and understand?

## MODIFY 🛠️

### Task 1: Menu System
Create a simple restaurant menu using a dictionary. Then write code that:
- Shows all available items
- Takes a user's order
- Displays the price, or "Item not available" if it's not on the menu

```

### Task 2: 🤔 Challenge Connection
Think back to your Rock Paper Scissors game with all those if/else statements checking combinations...

**Hint Questions:**
- What if player moves were keys in a dictionary?
- What if the values told you what each move beats?
- How might this make your RPS code cleaner?

Think about the possibilities!

## MAKE 🚀

Choose one of these projects:

### Project A: Personal Assistant Bot
Create a dictionary-based chatbot that responds to different greetings and questions:

```python
responses = {
    "hello": "Hi there! How can I help?",
    "how are you": "I'm doing great, thanks!",
    "bye": "Goodbye! Have a great day!"
    # Add more responses...
}
```

Make it handle unknown inputs gracefully and add at least 8 different responses.

### Project B: Simple Translator
Create a dictionary that translates English words to another language. Your programme should:
- Allow users to look up translations
- Add new word pairs
- Handle words that aren't in the dictionary yet

### Project C: Game Statistics Tracker
Create a system that tracks wins/losses for different games using nested dictionaries:

```python
game_stats = {
    "Kofi": {"wins": 0, "losses": 0},
    "Jasmine": {"wins": 0, "losses": 0}
}
```

Include functions to update stats and display leaderboards.

## Reflection Questions 💭

- When might dictionaries be more useful than lists?
- How do dictionaries make code more readable?
- What connections do you see between dictionaries and your previous Rock Paper Scissors project?
- What other coding problems have you encountered where dictionaries might help?

## Extension Challenges 🌟

Ready for more? Try these:

- **Dictionary Comprehensions:** Research and try creating dictionaries using comprehension syntax
- **Nested Dictionaries:** Create a student database with multiple pieces of information per student
- **Dictionary Methods:** Explore `.items()`, `.pop()`, and `.update()` methods
- **Real Data:** Find a dataset online and represent it using dictionaries

