
peole = ['John', 'Marry', 'Terry', 'Dan']


def generateInitial(names):
    tramsformed = []
    for name in names:
        tramsformed.append(name[0] + '.')
        return tramsformed

initials = generateInitial(peole)

print(initials)