# import sys

# x = input().strip().split(".")


# def isValid(x):
#     if len(x) != 4:
#         return 0
#     for i in x:
#         if int(i) != 0 and len(i) != len(str(int(i))):
#             return 0
#     return 1


# sys.stdout.write(str(isValid(x)))
import sys

x = input().strip()


def isit(s):
    try:
        return str(int(s)) == s and 0 <= int(s) <= 255
    except:
        return False
    try:
        return int(s, 16) >= 0 and s[0] != '-'
    except:
        return False


def isValid(st):
    if st.count(".") == 3 and all(isit(i) for i in st.split(".")):
        return 1
    return 0


sys.stdout.write(str(isValid(x)))
