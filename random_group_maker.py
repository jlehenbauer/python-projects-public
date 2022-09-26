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

    print("Sending to first station . . .")

    already_assigned = stations(people, num_stations, already_assigned)

def stations(people, num_stations, already_assigned):
    assignments = {(x+1):[] for x in range(num_stations)}
    for person in people:
        assignment = random.randint(1, num_stations)
        while assignment in already_assigned[person] or len(assignments[assignment]) >= len(people)/num_stations:
            assignment = random.randint(1, num_stations)
        already_assigned[person].append(assignment)
        assignments[assignment].append(person)

    print(assignments)

    return already_assigned


if __name__ == "__main__":
    main()