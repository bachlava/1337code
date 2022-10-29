"""
You are given a phone number as a string number.
number consists of digits, spaces ' ', and/or dashes '-'.
You would like to reformat the phone number in a certain manner.
Firstly, remove all spaces and dashes.
Then, group the digits from left to right into blocks of length 3
until there are 4 or fewer digits.
The final digits are then grouped as follows:
    2 digits: A single block of length 2.
    3 digits: A single block of length 3.
    4 digits: Two blocks of length 2 each.
The blocks are then joined by dashes.
Notice that the reformatting process should never produce any blocks
of length 1 and produce at most two blocks of length 2.
Return the phone number after formatting.
Constraints:
    2 <= number.length <= 100
    number consists of digits and the characters '-' and ' '.
    There are at least two digits in number.
"""
class Solution:
    def reformat_number(self, number: str) -> str:
        default_size = 3
        digits = ''.join([char for char in number if char.isdigit()])
        digit_groups = []
        while len(digits) > 4:
            digit_groups.append(digits[:default_size])
            digits = digits[default_size:]
        
        if len(digits) == 4:
            digit_groups.extend([digits[:2], digits[2:]])
        else:
            digit_groups.append(digits)

        result = '-'.join(digit_groups)
        return result


if __name__ == '__main__':
    number1 = '1-23-45 6'
    print(Solution().reformat_number(number1))
    number2 = '123 4-567'
    print(Solution().reformat_number(number2))
    number3 = '123 4-5678'
    print(Solution().reformat_number(number3))
