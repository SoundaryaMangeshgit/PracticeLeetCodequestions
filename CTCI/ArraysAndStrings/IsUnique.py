# Question 1
# IsUnique
# 1.1 Implement an algorithm to determine if a string has all unique characters

class Solution:
    def isUnique1(self, data):
        mapper = set()
        for i in data.lower():
            if i not in mapper:
                mapper.add(i)
            else:
                return False
        return True

    def isUnique2(self, data):
        return True


if __name__ == "__main__":
    sol = Solution()
    data = "TactCoa"
    print(f"{sol.isUnique1(data)} isUnique1")
    print(f"{sol.isUnique2(data)} isUnique2")

    