#Exercise 5
def letter_grade(score):
    if score > 100 :
        return "Invalid"
    elif score >= 97 :
        return "A+"
    elif 90 <= score  <= 96.9:
        return "A"
    elif 80 < score <= 89.9:
        return "B"
    elif 70 < score <= 79.9:
        return "C"
    elif 60 <= score <= 69.9:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid"

score_test = [99,90,85,5,72,60,59.9,-5,101]

for score in score_test:
    print(score,"->",letter_grade(score))