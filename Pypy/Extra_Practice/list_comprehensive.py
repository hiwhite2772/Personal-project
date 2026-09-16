ds = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    
    ds.append([name, score])

score_min = ds[0][1]
for score in ds:
    if score[1] < score_min:
        score_min = score[1]

remaining_scores= [score[1] for score in ds if score[1] != score_min]

second_lowest = min(remaining_scores)

names = [student[0] for student in ds if student[1] == second_lowest]

names.sort()

for name in names:
    print(name)