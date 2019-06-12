# get a valid number between 2 and 100
while True:
    n = int(input("Number of Students: "))
    if (n >= 2 and n <= 10):
        break
student_marks = {}
error = 0
for _ in range(n):
    name, *line = input("Student & Marks: ").split()
    scores = list(map(float, line))
    for i,j in enumerate(scores):
        if float(j) <= 0 or float(j) >= 100: # if score is not between 0 and 100, error
            error = 1
    if error < 1:
        student_marks[name] = scores # create dict
    else:
        break
if error < 1:
    query_name = input("Which Student: ")

studScore = []
scoreSum = 0
scoreCount = 0

# get average score
for k in student_marks:
    if k == query_name:
        studScore = student_marks[k]
        for l,m in enumerate(studScore):
            scoreSum += float(m)
            scoreCount += 1
averScore = scoreSum / scoreCount
print('{0:.2f}'.format(averScore)) # print with two decimal places
