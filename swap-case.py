def swap_case(s):
    contaner = ""
    for i in s:
        if i.isupper():
            contaner += i.lower()
        elif i.islower():
            contaner += i.upper()
        else:
            contaner += i
    return contaner
