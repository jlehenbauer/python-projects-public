import random as rand
import time


def make_lists(number_of_lists):
    # make an empty list
    l = []

    # make n items in that list
    for i in range(number_of_lists):
        m = rand.randint(0, 10000000)
        item = []
        # make each item a random length list of random numbers

        # start a timer
        start = time.time()

        # make new list of integers
        for y in range(m):
            item.append(rand.randint(0, 100))

        # add that list to the big list
        l.append(item)

        # stop timer
        end = time.time()

        # print item count and time taken
        print("Item " + str(len(l)) + " of length " + format(int(len(l[-1])), ",") + " added in " + str(end - start) + " seconds")
    return l


def sort_lists(lists):
    for item in lists:
        start = time.time()
        new_item = sorted(item)
        end = time.time()
        print(str(format(len(new_item), ",")) + ", " + str(end - start))


sort_lists(make_lists(20))