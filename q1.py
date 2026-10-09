'''
A college stores students' marks in a list. 
Write a function that accepts a list of marks and displays the highest mark, lowest 
mark, average mark, and number of students who passed (marks of 40 or above).
'''

def analyze_marks(marks: list):
    print('highest marks:', max(marks))
    print ('lowest marks:', min(marks))
    average = sum(marks)/len(marks)
    print("average mareks:", round(average, 2))
    count = 0
    for i in marks:
        if (i >= 40):
            count = count + 1
    print("no of students who passed is: ",count)

analyze_marks([58,74,32,56,98,64])
       