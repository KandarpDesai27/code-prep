'''
input = aabcccccaaa -> a2b1c5a3 (return original string if len(original) < len(compressed))

Time = O(n)
Space = O(n) since an array needed to construct compressed string

'''
def compressString(str1):

	if not str1:
		return str1 

	currentChar = str1[0]
	charCount = 1
	result = [str1[0]]
	
	for c in str1[1:]:
		if c == currentChar:
			charCount += 1
		else:
			result.append(str(charCount))
			result.append(str(c))
			currentChar = c
			charCount = 1
	result.append(str(charCount))

	return "".join(result) if len(result) < len(str1) else str1



print(compressString("aabcccccaaa"))
print(compressString("abcd"))
print(compressString("aaa"))