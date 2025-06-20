try:
    number = int(input("enter number"))
    print(1/ number)
except ZeroDivisionError:
    print("noooooo")
except ValueError:
    print("enter only numbers")
except Exception:
    print("inavlid")
finally:
    print("fix it")
