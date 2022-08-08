#CAMILY PEREIRA ALBRES 
#Implemente um código que faça a leitura de um arquivo txt sobre conjuntos, e faça operações de diferença,intersecção, produto cartesiano e união.

file = open('conjuntos2.txt')

content = file.readlines()

originalArray = [line.rstrip('\n').split(', ') for line in content]

removeFirstElement = originalArray.pop(0)

operationArray = []

for i in range(0,len(originalArray),3):
  operationArray.append(originalArray[i:i+3])

def removeRepeated(result):
  cleanResult = []
  for line in result:
   if line not in cleanResult:
     cleanResult.append(line)
  return cleanResult

def interface(operation,setA,setB,result):
  result = removeRepeated(result)
  setA = "{" + ", ".join(map(str, setA)) + "}"
  setB = "{" + ", ".join(map(str, setB)) + "}"
  result = "{" + ", ".join(map(str, result)) + "}"
  print(f"{operation}: conjunto 1 {setA}, conjunto 2 {setB}, Resultado: {result} \n")

def union(setA,setB):
  operation = "União"
  result = setA+setB
  interface(operation,setA,setB,result)
  return result

def intersection(setA,setB):
  operation = "Intersecção"
  result = [value for value in setA if value in setB] 
  interface(operation,setA,setB,result)
  return result
  
def difference(setA,setB):
  operation = "Diferença"
  result = [value for value in setA if value not in setB]
  interface(operation,setA,setB,result)
  return result
  
def cartesian(setA,setB):
  operation = "Produto cartesiano"
  #result = [i+(j) for i in setA for j in setB]
  result = []
  for i in setA:
    for j in setB: 
     result.append(f"[{i},{j}]")
  interface(operation,setA,setB,result)
  return result

mydict = {}
for index, operationLine in enumerate(operationArray):
 mydict[index] = operationLine
  
for key in mydict:
  
  operationLetter = mydict[key][0][0]
  
  if operationLetter == "U":
    union(mydict[key][1],mydict[key][2])
    
  elif operationLetter == "D":
    difference(mydict[key][1],mydict[key][2])
    
  elif operationLetter == "I":
    intersection(mydict[key][1],mydict[key][2])
    
  elif operationLetter == "C":
    cartesian(mydict[key][1],mydict[key][2])

