def compress(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1]
            if count > 1:
                result += str(count)
            count = 1

    result += s[-1]
    if count > 1:
        result += str(count)

    return result


def decompress(s):
    result = ""
    i = 0

    while i < len(s):
        ch = s[i]
        i += 1

        num = ""

        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        if num:
            result += ch * int(num)
        else:
            result += ch

    return result


s = input("Enter String: ")

compressed = compress(s)

print("Compressed:", compressed)
print("Decompressed:", decompress(compressed))