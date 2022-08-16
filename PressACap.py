
def pressAforCapsLock(s):
    if not s:
        return
    if len(s)==1:
        if s == 'a' or s == 'A':
            return
        else:
            return s

    CapsLock = False
    result = ''

    for char in s:
        if char == 'a' or char == 'A':
            CapsLock = not CapsLock
            continue

        if CapsLock:
            if char.islower():
                result += char.upper()
            elif char.isupper():
                result += char.lower()
            else: result += char
        else: result += char
    return result

print(pressAforCapsLock('My keboard is broken!'))





