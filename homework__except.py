error_code=1
while error_code !=0:

 a = input('Введите операцию :')
 b=a.strip().split(' ')
 try:
   operand_1 = int(b[1])
   operand_2 = int(b[2])
   assert (operand_1 >= 0) & (operand_2 >=0) 
 except AssertionError:
   print('Числа должны быть положительными')
 except:
   print('Введены некорректные данные')
 else:
   error_code=0
 if b[0] !=('+' or '-' or '*' or '/'):
   error_code=1
   print('Некорректно введен знак операции')

 
if b[0] =='+':
  result = operand_1+operand_2 
elif b[0] =="-":
  result = operand_1-operand_2 
elif b[0] =="*":
  result = operand_1*operand_2 
elif b[0] =="/":
  result =operand_1/operand_2 

print(result)
