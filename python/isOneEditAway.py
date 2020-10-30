'''
Time O(n)
Space O(1)
'''
def isOneEditAway(str1, str2):
	if abs(len(str1) - len(str2)) > 1:
		return False

	if len(str1) == len(str2):
		return isOneReplaceAway(str1, str2, "edit")

	if len(str1) > len(str2):
		return isOneReplaceAway(str1, str2, "add")

	if len(str1) < len(str2):
		return isOneReplaceAway(str2, str1, "add")


def isOneReplaceAway(str1, str2, operation):
	idx1 = 0
	idx2 = 0
	isEdited = False

	while idx1 < len(str1):
		if str1[idx1] != str2[idx2]:
			if isEdited:
				return False
			else:
				isEdited = True
				if operation == "add":
					idx1 += 1
					continue
		idx1 += 1
		idx2 += 1
	return True


print(isOneEditAway("pale", "bale"))
print(isOneEditAway("pale", "ple"))
print(isOneEditAway("ple", "pale"))
print(isOneEditAway("kalp", "pale"))
print(isOneEditAway("please", "pale"))			
