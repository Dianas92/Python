a = input('Введите операцию :')
b=a.strip().split(' ')
try:
 operand_1 = int(b[1])
 operand_2 = int(b[2])
 assert (operand_1 >= 0) & (operand_2 >=0) 
except:
 print('Введено некорректное выражение')
else:
 result= 'Невозможно вычислить'
 
 if b[0] =='+':
   result = operand_1+operand_2 
 elif b[0] =="-":
   result = operand_1-operand_2 
 elif b[0] =="*":
   result = operand_1*operand_2 
 elif b[0] =="/":
   result =operand_1/operand_2 

 print(result)
