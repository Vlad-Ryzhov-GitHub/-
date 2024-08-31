grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_students = sorted(students)
average_score = {}
ave1 = sum(grades[0]) / len(grades[0])
ave2 = sum(grades[1]) / len(grades[1])
ave3 = sum(grades[2]) / len(grades[2])
ave4 = sum(grades[3]) / len(grades[3])
ave5 = sum(grades[4]) / len(grades[4])

average_score[list_of_students[0]] = ave1
average_score[list_of_students[1]] = ave2
average_score[list_of_students[2]] = ave3
average_score[list_of_students[3]] = ave4
average_score[list_of_students[4]] = ave5
print(average_score)