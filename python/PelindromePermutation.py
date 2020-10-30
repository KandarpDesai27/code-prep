'''
Time = O(n)
Space = O(1) Assuming there are only  english chars
'''
def isPelindromeForPermutations(word):
	word = word.lower().replace(" ", "")
	frequencySet = set()

	for c in word:
		if c in frequencySet:
			frequencySet.remove(c)
		else:
			frequencySet.add(c)

	if len(frequencySet) > 1:
		return False

	return True

print(isPelindromeForPermutations("aabb"))        #True
print(isPelindromeForPermutations("Tact coa"))    #True
print(isPelindromeForPermutations("aabbx"))       #True
print(isPelindromeForPermutations("abcd"))        #False
print(isPelindromeForPermutations("xy"))          #False