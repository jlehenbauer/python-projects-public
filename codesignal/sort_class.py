def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort()
    return list(map(str, res))


class CodeSignalUser(object):
    def __init__(self, user, _id, xp):
        self.name = str(user)
        self._id = _id
        self.xp = xp
        return

    def __lt__(self, other):
        if self.xp != other.xp:
            return int(self.xp) < int(other.xp)
        return int(self._id) < int(other._id)

    def __str__(self):
        return self.name

users1 = [["warrior", "1", "1050"],["Ninja!",  "21", "995"],["recruit", "3", "995"]]
users2 = [["Corrie","66","5"],["Arie","99","8"],["Joann","32","5"],["Larhonda","9","9"],["Leda","38","7"],["Anabel","68","3"],["Javier","10","7"],["Vicente","49","9"],["Deanna","29","6"],
 ["Tracie","28","7"],["Stephaine","1","8"],["Yaeko","2","10"],["Jared","27","8"],["Fernando","55","10"],["Sarita","90","9"],["Erlene","35","2"],["Kandace","12","9"],["Jeane","37","7"],["Malika","80","4"],["Malinda","92","7"]]
print(sortCodesignalUsers(users1))
print(users1)
print("")
print("****")
print("")
print(sortCodesignalUsers(users2))
print(users2)