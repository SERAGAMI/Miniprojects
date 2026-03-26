f = int(input("enter number:"))
d = input("enter operation+,-,%,//,/ *,**:")
s = int(input("enter number:"))
if d == "+":
    result = f + s
    print(result)
elif d == "-":
    result = f - s
    print(result)
elif d == "%":
    result = f % s
    print(result)
elif d == "*":
    result = f * s
    print(result)
elif d == "**":
    result = f ** s
    print(result)
elif d == "//":
    result = f // s
    print(result)
elif d =="/":
    result = f / s
    print(result)
else:
    print("Wrong input or operation")