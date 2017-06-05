def findMinimo(array):
	
	minimo = array[0]
	
	for num in array:
		
		if(num < minimo):
			
			minimo = num
	
	return num

array = map(int, raw_input().split())

print(findMinimo(array))
	
