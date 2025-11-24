📝 1. Introduction

Learning a new language often requires memorizing vocabulary. Traditionally, students use flashcards to practice word meanings.
This project presents a Python-based vocabulary quiz program that automates this process and provides an interactive way to learn English–Spanish word pairs.

The program loads vocabulary from text files, quizzes the user, checks answers, and allows saving incorrect responses for further revision.
It is simple, efficient, and useful for language learners.


---

🎯 2. Objectives

The primary objectives of this project are:

To develop a vocabulary quiz application using Python.

To load English–Spanish word lists from text files.

To test the user on randomly selected words.

To check correctness and score the user.

To save missed words into a separate file for revision.

To provide a practical alternative to physical flashcards.



---

🧠 3. Problem Statement

Students often struggle to memorize vocabulary when learning a foreign language.
Manual flashcards are effective but time-consuming to create and organize.

This project aims to create a computer-based quiz program that:

Reads vocabulary word lists from files,

Randomly quizzes the user,

Tracks correct and incorrect answers,

Saves missed words for later practice.


This provides an efficient and interactive learning tool.


---

🏗 4. System Requirements

Software Requirements

Python 3.x

Text editor (VS Code, Notepad++, PyCharm, etc.)


Hardware Requirements

Basic computer or laptop

Minimum 2 GB RAM

Any operating system (Windows/Linux/macOS)
🔍 5. Vocabulary File Format

Each vocabulary file must end with .txt and follow this format:

english_word: spanish1, spanish2, ...

Example:

study: estudiar
search: buscar, mirar
be: ser, estar

These files act as mini-dictionaries for the quiz.


---

🧩 6. Program Logic / Flow

Step-by-step Description

1. List all .txt vocabulary files in the folder.


2. Ask the user to select a valid file.


3. Load contents into a Python dictionary.


4. Display the number of words available.


5. Ask user how many words they want to be quizzed on.


6. Randomly select that many English words.


7. Ask user to input the Spanish equivalents.


8. Check answers and keep score.


9. Display final result.


10. Allow user to save missed words in a new file.