student_scores = {
    "Praise":85,"Shaun":90,"Gavi":92,"Mango":95
    }

student_grades ={}

for key in student_scores:
    if student_scores[key] >90:
        student_grades[key]="Outstanding"
    elif student_scores[key] >80 and student_scores[key] <=90:
        student_grades[key] ="Exceed exceptional"
print(student_grades)