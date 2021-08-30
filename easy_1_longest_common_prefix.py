# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0 or strs == "":
            return ""
        elif len(strs) == 1:
            return strs[0]

        str_lens = []
        sub_str = ""

        for word in strs:
            str_lens.append(len(word))
        max_length = min(str_lens)

        for i in range(0, max_length):
            temp = []
            char = strs[0][i]
            for word in strs:
                if char != word[i]:
                    break
                else:
                    temp.append(char)

            if temp and len(temp) == len(strs):
                sub_str += temp[0]
            else:
                break

        return sub_str


my_solution = Solution()
strs = ["flower", "flow", "flight"]
print(my_solution.longestCommonPrefix(strs))
