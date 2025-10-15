import os
import random

# Create quiz folder
os.makedirs("quiz", exist_ok=True)

# Question papers by topic
question_papers = {
    1: {
        "topic": "Mathematical Operators",
        "questions": [
            "What is 15 + 25?",
            "Calculate 100 - 67",
            "What is 8 × 9?",
            "What is 144 ÷ 12?",
            "What is 2^5 (2 to the power of 5)?",
            "What is 17 % 5 (17 modulo 5)?",
            "Calculate 45 + 33 - 28",
            "What is 7 × 6 ÷ 2?",
            "What is the square of 12?",
            "Calculate 200 ÷ 8 + 15"
        ]
    },
    2: {
        "topic": "Python Programming",
        "questions": [
            "What keyword is used to define a function in Python?",
            "Which symbol is used for comments in Python?",
            "What is the output of print(type([]))?", 
            "How do you create a list in Python?",
            "What does 'len()' function do?",
            "Which loop is used to iterate over a sequence?",
            "What is the difference between '==' and 'is'?",
            "How do you import a module in Python?",
            "What is indentation used for in Python?",
            "Which function is used to get user input?"
        ]
    },
    3: {
        "topic": "General Knowledge",
        "questions": [
            "What is the capital of India?",
            "Who invented the telephone?",
            "What is the largest ocean in the world?",
            "In which year did India gain independence?",
            "Who painted the Mona Lisa?",
            "What is the chemical symbol for gold?",
            "Which is the smallest planet in our solar system?",
            "Who wrote 'Romeo and Juliet'?",
            "What is the currency of Japan?",
            "Which mountain range contains Mount Everest?"
        ]
    },
    4: {
        "topic": "Science & Technology",
        "questions": [
            "What is the chemical formula for water?",
            "Who is known as the father of computers?",
            "What does CPU stand for?",
            "What is the speed of light?",
            "Which gas do plants absorb from the atmosphere?",
            "What is the unit of electric current?",
            "Who developed the theory of relativity?",
            "What does HTML stand for?",
            "What is the boiling point of water in Celsius?",
            "Which vitamin is produced by skin when exposed to sunlight?"
        ]
    },
    5: {
        "topic": "History & Geography",
        "questions": [
            "Who was the first Prime Minister of India?",
            "Which river is the longest in the world?",
            "In which year did World War II end?",
            "What is the largest continent?",
            "Who built the Taj Mahal?",
            "Which desert is the largest in the world?",
            "Who was the first person to walk on the moon?",
            "What is the smallest country in the world?",
            "Which empire was ruled by Julius Caesar?",
            "What is the deepest ocean trench?"
        ]
    }
}

# Create 5 question papers
for paper_num, paper_data in question_papers.items():
    filename = f"quiz/Questions{paper_num}.txt"
    
    with open(filename, "w") as f:
        f.write(f"QUESTION PAPER {paper_num}\n")
        f.write(f"Topic: {paper_data['topic']}\n")
        f.write("="*50 + "\n\n")
        
        for i, question in enumerate(paper_data['questions'], 1):
            f.write(f"Q{i}. {question}\n\n")
        
        f.write("="*50 + "\n")
        f.write("End of Question Paper\n")
    
    print(f"Created {filename} - Topic: {paper_data['topic']}")

print("\nAll question papers created successfully!")

# List files in quiz folder
print(f"\nFiles in quiz folder: {os.listdir('quiz')}")

# Show sample from mathematical operators paper
print("\n" + "="*50)
print("SAMPLE: Mathematical Operators Question Paper")
print("="*50)
with open("quiz/Questions1.txt", "r") as f:
    print(f.read())