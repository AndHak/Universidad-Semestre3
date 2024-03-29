"""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

Examples
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
"""
def balanced_parens(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result

# Ejemplos
print(balanced_parens(0))  # => [""]
print(balanced_parens(1))  # => ["()"]
print(balanced_parens(2))  # => ["()()", "(())"]
print(balanced_parens(3))  # => ["()()()", "(())()", "()(())", "(()())", "((()))"]
