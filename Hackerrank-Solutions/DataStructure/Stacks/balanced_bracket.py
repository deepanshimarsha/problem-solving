def isbalanced(s):
	opening = ['(', '{', '[']
	closing = [')', '}', ']']
	pair = ['()', '{}', '[]']
	stack = []
	for i in range(0, len(s)):
		if s[i] in opening:
			stack.append(s[i])
		elif s[i] in closing:
			if len(stack) == 0 or stack[-1]+s[i] not in pair:
				return "NO"
			else:
				return "YES"
	if len(stack) == 0:
		return "YES"
	else:
		return "NO"


print(isbalanced("{[(]}"))
