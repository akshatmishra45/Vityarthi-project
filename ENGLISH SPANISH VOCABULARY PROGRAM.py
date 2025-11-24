#ENGLISH SPANISH VOCABULARY PROGRAM: 

import os
import random

def list_vocab_files():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    print("Select one of the following word lists:")
    for f in files:
        print(f)
    return files

def load_dictionary(filename):
    vocab = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                eng, span = line.split(":")
                eng = eng.strip()
                span_words = [w.strip() for w in span.split(",")]
                vocab[eng] = span_words
    return vocab

def quiz_user(vocab, num_words):
    english_words = list(vocab.keys())
    random.shuffle(english_words)
    selected = english_words[:num_words]

    wrong_answers = []
    score = 0

    for eng in selected:
        correct_answers = vocab[eng]
        print(f"\nEnglish word: {eng}")
        print(f"Enter {len(correct_answers)} equivalent Spanish word(s).")

        user_inputs = []
        for i in range(len(correct_answers)):
            ans = input(f"Word [{i+1}]: ").strip().lower()
            user_inputs.append(ans)

        # Check correctness
        if all(user_inputs[i] == correct_answers[i].lower() for i in range(len(correct_answers))):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            wrong_answers.append(f"{eng} : {', '.join(correct_answers)}")

    return score, wrong_answers

def save_wrong_answers(wrong_list, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for item in wrong_list:
            f.write(item + "\n")
    print(f"Saved wrong answers to {output_file}")


# -------------------------------
#            MAIN PROGRAM
# -------------------------------

print("Welcome to the vocabulary quiz program.")

files = list_vocab_files()

# Step 2: User chooses a file
filename = input("Please make your selection: ").strip()

while filename not in files:
    print("Invalid file name! Try again.")
    filename = input("Please make your selection: ").strip()

# Step 3: Load dictionary
vocab = load_dictionary(filename)

print(f"{len(vocab)} entries found.")

# Step 5: Number of questions
while True:
    try:
        n = int(input("How many words would you like to be quizzed on? "))
        if 1 <= n <= len(vocab):
            break
        else:
            print("Enter a valid number.")
    except ValueError:
        print("Enter a number only!")

# Step 6: Quiz
score, wrong = quiz_user(vocab, n)

print(f"\n---\n{score} out of {n} correct.")

# Step 7: Save wrong answers
output_file = input("Enter an output file (or press Enter to quit): ").strip()

if output_file != "":
    save_wrong_answers(wrong, output_file)

print("Program finished.")