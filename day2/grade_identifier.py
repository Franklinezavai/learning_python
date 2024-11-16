attained_score = int(input("enter your score: "))

if attained_score >= 80:
    grade = "A"
elif 70 <= attained_score < 80:
    grade = "D"
elif 60 <= attained_score < 70:
    grade = "C"
elif 50 <= attained_score < 60:
    grade = "D"
elif 40 <= attained_score < 50:
    grade ="E"
elif attained_score < 40 :
    grade = "F"
else:
    grade = ('input not found')
print(grade)