class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
            if s == goal:
                return True

            s, goal = [*s], [*goal] 

            # unpacking the strings (creates list)
            # ex: 'hello' -> ['h','e','l','l','o']


            for x in range(len(s)):
                a = s[0]
                s.pop(0); s.append(a)
                # rotate the string by saving the first character then removing it and then adding it to the end

                if s == goal:
                    return True
                # checking if the rotated string is the same as the goal

            return False