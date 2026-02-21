x = input("Enter your calculation: ")

number = []
operations = []
num = ""

for ch in x:
    if ch.isdigit():
        num += ch
    else:
        number.append(float(num))
        operations.append(ch)
        num = ""
number.append(float(num))

bodmas = ['^','%','/', '*', '+', '-']

for op in bodmas: 
    i = 0
    while i < len(operations):
        if operations[i] == op:
            if op == '+':
                result = number[i] + number[i+1]
            elif op == '-':
                result = number[i] - number[i+1]
            elif op == '*':
                result = number[i] * number[i+1]
            elif op == '/':
                result = number[i] / number[i+1]
            elif op == '^':
                result = number[i] ** number[i+1]
            elif op == '%':
                result = (number[i] * number[i+1]) /100    

            number[i] = result
            number.pop(i+1)
            operations.pop(i)
        else:
            i += 1


print("Result is: ", number[0])
