Rule-Based Disease Diagnosis System


Overview:


This project is a simple rule-based medical expert system implemented in Python.
It asks users about common symptoms and suggests possible diseases based on predefined rules.
The system does not use machine learning. It relies entirely on deterministic rule matching (if–then logic).



How It Works:


The system contains a knowledge base of diseases and their required symptoms.

The user answers yes/no questions about symptoms.

The program collects the selected symptoms.

It checks whether all required symptoms of a disease are present.

If a full match is found, the disease is suggested.




The inference logic is based on:

If all symptoms of a disease are present → suggest that disease




Knowledge Base (Current Rules):


Flu → fever, cough, fatigue

Cold → cough, sneezing

COVID → fever, cough, loss_of_taste

Malaria → fever, chills, headache




How to Run:

Requirements:
Python 3.x


Run the program:
python main.py



Example Output:


Answer with yes(y) or no(n)

Do you have fever? (y/n) y
Do you have cough? (y/n) y
Do you have fatigue? (y/n) n
Do you have sneezing? (y/n) n
Do you have loss_of_taste? (y/n) y
Do you have chills? (y/n) n
Do you have headache? (y/n) n

Possible Diagnosis:
- COVID




Features:

Simple command-line interface

Rule-based inference engine

Easy to extend knowledge base

Lightweight and beginner-friendly




Limitations:


No probability scoring

No severity analysis

Can return multiple diseases if rules overlap

Only works with predefined diseases

Not intended for real medical diagnosis




Future Improvements:


Add symptom weighting

Add match percentage scoring

Implement probabilistic reasoning (Bayesian approach)

Convert to GUI or web-based system

Store rules in external file or database




Disclaimer

This project is for educational purposes only and should not be used for real medical diagnosis. Always consult a qualified healthcare professional.