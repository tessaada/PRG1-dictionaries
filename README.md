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

Run the code in `predict1.py` and see if you were right.

Now try these experiments:

## INVESTIGATE 🕵️‍♀️

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

## INVESTIGATE (Continued) 🔍

### Your Turn to Experiment

### Comparing Approaches: If/Else vs Dictionaries

One of the most powerful uses of dictionaries is replacing long chains of if/else statements. Let's compare two approaches:

**Approach A: Multiple if/else statements**
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

**Approach B: Dictionary lookup**
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

**Discussion Questions:**
- Which approach uses fewer lines of code?
- Which would be easier to add 10 more colours to?
- Which is easier to read and understand?
- Can you think of other situations where this pattern would be useful?

## MODIFY 🛠️

Now it's time to apply what you've learned by modifying and extending dictionary code.

### Task 1: Restaurant Menu System 

Create a simple restaurant menu using a dictionary (See `restaurant.py`). Your program should:
1. Display all available items and their prices
2. Take a user's order
3. Display the price, or show "Item not available" if it's not on the menu

```python
menu = {
    "pizza": 8.99,
    "burger": 6.50,
    "salad": 5.25,
    # Add at least 3 more items
}

# Your code here
```

### Task 2: Challenge Connection 🤔

Think back to your Rock Paper Scissors game with all those if/else statements checking win conditions...

**Hint Questions to explore:**
- What if you created a dictionary where player moves were keys?
- What if the values told you what each move beats?
- Could you use a nested dictionary to store all win conditions?
- How might this approach make your RPS code cleaner and easier to extend?

Take a few minutes to sketch out how you might refactor your Rock Paper Scissors code using a dictionary.

## MAKE 🚀

Choose one project to build from scratch. Challenge yourself to use dictionaries effectively!

### Project A: Personal Assistant Chatbot

Create a dictionary-based chatbot that responds to different greetings and questions.

**Requirements:**
- Include at least 8 different input-response pairs
- Handle unknown inputs gracefully with a default message
- Make responses friendly and varied

**Starter code:**  (You can create yourself a new .py file for this code)
```python
responses = {
    "hello": "Hi there! How can I help?",
    "how are you": "I'm doing great, thanks!",
    "bye": "Goodbye! Have a great day!",
    # Add at least 5 more responses
}

# Your code here to make the chatbot interactive
```

**Extension ideas:**
- Add multiple possible responses for each input (using lists as values)
- Make the bot respond to partial matches
- Keep a conversation history

### Project B: Simple Translator

Create a dictionary that translates English words to another language you know.

**Requirements:**
- Start with at least 10 word pairs
- Allow users to look up translations
- Allow users to add new word pairs during the programme
- Handle words that aren't in the dictionary yet with a helpful message

**Extension ideas:**
- Add the ability to translate in both directions
- Save new words to a file
- Create a quiz mode to test vocabulary

### Project C: Game Statistics Tracker

Create a system that tracks wins, losses, and draws for different players across multiple games.

**Requirements:**
- Use nested dictionaries to store player statistics
- Include functions to update statistics after each game
- Display a leaderboard showing player rankings
- Calculate win percentages

**Starter structure:**
```python
game_stats = {
    "Kofi": {"wins": 0, "losses": 0, "draws": 0},
    "Jasmine": {"wins": 0, "losses": 0, "draws": 0}
}

def update_stats(player, result):
    # Your code here
    pass

def display_leaderboard():
    # Your code here
    pass
```

**Extension ideas:**
- Track statistics for different game types
- Add a player comparison feature
- Include timestamps for recent games

## Reflection Questions 💭

Take a moment to think about what you've learned:

- When might dictionaries be more useful than lists?
- How do dictionaries make code more readable and maintainable?
- What connections do you see between dictionaries and your previous Rock Paper Scissors project?
- What other coding problems have you encountered where dictionaries might help?
- What was the most surprising thing you learned about dictionaries today?

