rules = {
    "Flu": ["fever", "cough", "fatigue"],
    "Cold": ["cough", "sneezing"],
    "COVID": ["fever", "cough", "loss_of_taste"],
    "Malaria": ["fever", "chills", "headache"]
}

print("Answer with yes(y) or no(n)\n")

user_symptoms = []

for s in ["fever", "cough", "fatigue", "sneezing", "loss_of_taste", "chills", "headache"]:
    if input(f"Do you have {s}?(y/n) ").lower() == "y":
        user_symptoms.append(s)

print("\nPossible Diagnosis:")

found = False
for disease in rules:
    if all(symptom in user_symptoms for symptom in rules[disease]):
        print("-", disease)
        found = True

if not found:
    print("No disease matched. Consult a doctor.")
