'''
An online store maintains a list of mobile prices. Write a function 
to display all mobiles costing more than ₹20,000, calculate the 
total inventory value, and find the most expensive mobile price.
'''

def mobiles(price):
    count = []
    for i in price:
        if (i>20000):
            count.append(i)
    total = 0
    for i in price:
    total = total + i
    highest = max(price)
    print('all mobiles more than 20k are: ',count)
    print('total price of all mobiles:', total)
    print('highest mobile prices:',highest)


mobiles([15000,20000,40000,62000])