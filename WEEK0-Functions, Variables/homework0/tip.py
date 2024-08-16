def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    temp=float(d)
    return temp


def percent_to_float(p):
    temp=float(p.strip('%'))
    temp2=float(temp/100)
    return temp2


main()