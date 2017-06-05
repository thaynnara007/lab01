def findMaximo(array):
	
	maximo = array[0]
	
	for num in array:
		
		if(num > maximo):
			
			maximo = num
	
	return maximo

array = map(int, raw_input().split())

print(findMaximo(array))
