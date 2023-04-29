from typing import List
from Spring import Spring

class SpringArray:
    @staticmethod
    def equivalent_spring(spring_expr: str, springs: List[Spring]) -> Spring:
        spring_map = {str(i): spring for i, spring in enumerate(springs)}
        stack = []

        for char in spring_expr:
            if char.isdigit():
                stack.append(spring_map[char])

            elif char in {'{', '['}:
                stack.append(Spring())

            elif char in {'}', ']'}:
                spring2, spring1 = stack.pop(), stack.pop()

                new_spring = spring1.in_series(spring2) if char == '}' else spring1.in_parallel(spring2)
                stack.append(new_spring)

        return stack[0] if stack else Spring()
