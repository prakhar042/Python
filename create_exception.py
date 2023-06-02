class InvaildAgeException(Exception):
    pass
num = int(input("enter the age of person:"))
if num<18:
    raise InvaildAgeException
else:
    print('Eligible to vote:')
    
