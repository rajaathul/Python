"""Is the given list divisible by 3 or NOT?"""
harvest=[24,12,45,33,46,52,63,34,45,24,60,57]
list1=[]
for num in harvest:
    if num%3==0:
        list1.append(num)
print("The numbers divissible by 3 are: ",list1) 

"""Square of even numbers in a list"""
evensqr=[]
for i in harvest:
    if i%2==0:
        i=i*i
        evensqr.append(i)
print("The square of even numbers are: ",evensqr)

"""Sum of digits of all EVEN numbers in a list"""
even=[]
for s in harvest:
    if s%2==0:
        even.append(s)
print("Sum of even numbers are:",(sum(even)))

"""Remove duplicate numbers in a list"""
dup=[]
for x in harvest:
    if x not in dup:
        dup.append(x)
print("The list after removing Duplicates: ",dup)

"""Write a function birthDate() that takes the full name of your employees(as a string) and
displays the given employee’s birthdate."""
employees = {
    'Umesh': '5 November 1988',
    'Hari': '25 October 1987',
    'Manish': '10 September 1989',
    'Rohit': '30 April 1987',
    'Ravindra': '6 December 1988',
    'Pranav': '11 October 1993',
}

def birthDate():
    name=input("Enter the name: ")
    print(employees.get(name))
birthDate()


    



    
