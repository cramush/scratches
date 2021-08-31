# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21
#
# Example 4:
# Input: x = 0
# Output: 0

# class Solution:
    # def reverse(self, x: int) -> int:


class Solution:
    def reverse(self, x: int) -> int:

        if x <= -2 ** 31 or x >= 2 ** 31 - 1:
            return 0

        if x == 0:
            return 0

        else:

            str_x = str(x)
            new_list = []
            reverse_list = []

            for i in str_x:
                new_list.append(i)

            if new_list[-1] == "0":
                new_list.pop(-1)

            if new_list[0] == "-":
                q = new_list.pop(0)
                new_list.append(q)

            for i in range(len(new_list)):
                w = new_list.pop(-1)
                reverse_list.append(w)
            reverse_list = int("".join(reverse_list))
            if reverse_list <= -2 ** 31 or reverse_list >= 2 ** 31 - 1:
                return 0
            return reverse_list


sol = Solution()
print(sol.reverse(x = 2147483646))
