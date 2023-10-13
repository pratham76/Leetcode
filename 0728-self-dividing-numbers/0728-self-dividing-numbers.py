class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num):
            original_num = num
            while num > 0:
                digit = num % 10
                if digit == 0 or original_num % digit != 0:
                    return False
                num //= 10
            return True

        self_dividing_numbers = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                self_dividing_numbers.append(num)

        return self_dividing_numbers
        