import random

def main():
    print("How many people need to be put in groups? ")
    num_people = int(input("Enter a number: "))
    #while num_people != int(num_people):
    #    num_people = input("Enter a number: ")

    people = []
    for i in range(num_people):
        people.append(input(f"Enter person {i+1}'s name: "))
    
    print("How many stations do you need? ")
    num_stations = int(input("Enter a number: "))
    #while num_stations != int(num_people):
    #    num_stations = input("Enter a number: ")

    already_assigned = {person:[] for person in people}

    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

    i = 1

    while len(already_assigned[list(already_assigned.keys())[-1]]) < num_stations:

        print(f"Sending to {ordinal(i)} station . . .")
        i += 1

        already_assigned = stations(people, num_stations, already_assigned)

        input("Press enter to continue")

    print("Done! Every student has been to every station:")
    print(already_assigned)

def stations(people, num_stations, already_assigned):
    assignments = {(x+1):[] for x in range(num_stations)}
    for person in people:
        assignment = random.randint(1, num_stations)
        # TODO: hangs if current person cannot be assigned due to possible groups already being full
        while assignment in already_assigned[person] or len(assignments[assignment]) >= len(people)/num_stations:
            assignment = random.randint(1, num_stations)
        already_assigned[person].append(assignment)
        assignments[assignment].append(person)

    print(assignments)

    return already_assigned


if __name__ == "__main__":
    main()