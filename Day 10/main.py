expr = input("Enter the expression: ")
if '+' in expr:
    a,b = expr.split('+')
    print("Sum: ",int(a)+int(b))
elif '-' in expr:
    a,b = expr.split('-')
    print("Diff: ",int(a)-int(b))
elif '*' in expr:
    a,b = expr.split('*')
    print("Product: ",int(a)*int(b))
elif '/' in expr:
    a,b = expr.split('/')
    print("Div: ",int(a)/int(b))
else:
    print("Invalid option")