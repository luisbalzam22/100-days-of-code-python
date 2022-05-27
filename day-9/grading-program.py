student_scores: "dict[str, int]" = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

scores_msgs: "dict[str, str]" = {
    "best": "Outstanding",
    "above_avg": "Exceeds Expectations",
    "average": "Acceptable",
    "fail": "Fail"
}

student_grades: "list[str, str]" = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = scores_msgs["best"]
    elif student_scores[key] > 80:
        student_grades[key] = scores_msgs["above_avg"]
    elif student_scores[key] > 70:
        student_grades[key] = scores_msgs["average"]
    else:
        student_grades[key] = scores_msgs["fail"]

    # WHICH IS BETTER, MORE READABLE CODE: ABOVE OR BELOW?
    
    # if student_scores[key] > 90:
    #     student_grades[key] = scores_msgs["best"]
    # if student_scores[key] > 80 and student_scores[key] <= 90:
    #     student_grades[key] = scores_msgs["above_avg"]
    # if student_scores[key] > 70 and student_scores[key] <= 80:
    #     student_grades[key] = scores_msgs["average"]
    # if student_scores[key] <= 69:
    #     student_grades[key] = scores_msgs["fail"]


# 🚨 Don't change the code below 👇
print(student_grades)
