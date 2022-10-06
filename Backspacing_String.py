s=input()
t=input()
def b(S):
    ans = []
    for c in S:
        if c != '#':
            ans.append(c)
        else:
            ans.pop()
    return "".join(ans)
print(b(s)==b(t))