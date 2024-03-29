"""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

Examples
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
"""
def balanced_parens(n):
    generate_parens = lambda partial, left, right: [partial] if left == right == 0 else \
        (generate_parens(partial + "(", left - 1, right) if left > 0 else []) + \
        (generate_parens(partial + ")", left, right - 1) if right > left else [])
    
    return generate_parens("", n, n)


# Output
print(balanced_parens(0))  # => [""]
print(balanced_parens(1))  # => ["()"]
print(balanced_parens(2))  # => ["()()", "(())"]
print(balanced_parens(3))  # => ["()()()", "(())()", "()(())", "(()())", "((()))"]
