class Solution:
    def isValid(self, s):
        a = {"(": ")", "[": "]", "{": "}"}
        my_index = 0
        copy = list(s)
        for i in copy:
            """"print(s.index(a[i]) == my_index+1)
            print(s.index(a[i]))
            print(my_index+1)
            print(copy)
            print(i)"""
            if i in a.keys() and a[i] in s and copy.index(a[i]) == my_index+1:
                copy.remove(a[i])
            else:
                return False
            my_index += 1
        return True

test = Solution()
test_subject = "{[]}"
result = test.isValid(test_subject)
print(result)


