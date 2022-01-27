code, interactor, checker = int(input()), int(input()), int(input())
res = interactor
if interactor == 0:
    if code != 0: res = 3
    elif code == 0: res = checker
elif interactor == 1: res = checker
elif interactor == 4:
    if code != 0: res = 3
    elif code == 0: res = 4
elif interactor == 6: res = 0
elif interactor == 7: res = 1
print(res)