def greet(text):
    return text.title()+'!!'

me_obj=greet
you_obj = greet

func_list=[me_obj,you_obj,str.lower,str.upper]
print(func_list[0]('korea,fighting'))
print(func_list[3]('happy'))

for f in func_list:
    print(f('Hello, good time'))