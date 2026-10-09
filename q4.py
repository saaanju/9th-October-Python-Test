'''
A company stores employee salaries in a list. Write a function to 
calculate the average salary, display salaries above the average, 
and increase every salary by 10%.
'''

def empsal(salary:list):
    average = sum(salary)/len(salary)
    above_avg = []
    for i in salary:
        above_avg.append(i)
        increase_sal=[]
        for i in salary:
        increase_sal.append(i+(i*0.1))
    print("average salary is:",average)
    print("salaries above average are:",above_avg)
    print("increased salaries are:",increased_sal)

empsal([45000,2000,85000,65000])