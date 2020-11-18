start= int(input('enter start number: '))
end= int(input('enter end number: '))
for number in range (start , end+1 , 2):
    print (number)
print("--------")
for number in range (start+1 , end+1 ,2):
    print (number)
