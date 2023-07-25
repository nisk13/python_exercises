def main(names):
    for i, x in enumerate(names,1):
        if x == "Angy":
            print("{0}.My name is {1}".format(i,x))
        else:
            print("{0}.{1} is my classmate".format(i,x))

if __name__ == "__main__":
    names = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    main(names)
    