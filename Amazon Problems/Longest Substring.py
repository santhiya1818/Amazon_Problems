s = input("Enter String: ")

seen = {}
start = 0
ans = 0

for end in range(len(s)):

    if s[end] in seen and seen[s[end]] >= start:
        start = seen[s[end]] + 1

    seen[s[end]] = end

    ans = max(ans, end - start + 1)

print(ans)