from math import *

class Miflaga:
    def __init__(self, votes, name, mandats=0):
        self.votes = int(votes)
        self.name = name
        self.mandats = mandats
    def __str__(self):
        return f"{self.votes} {self.name} {self.mandats}"
    def __repr__(self):
        return str(self)

class Reshima:
    def __init__(self, votes, miflaga, miflaga2, mandats=None, modedNext=None):
        self.votes = votes
        self.miflaga = miflaga
        self.miflaga2 = miflaga2
        self.mandats = mandats
        self.odafim = 0
        self.modedNext = modedNext
    def __str__(self):
        if self.miflaga2:
            return f"{self.votes} {self.miflaga.name} {self.miflaga2.name} {self.mandats} {self.odafim}"
        return f"{self.votes} {self.miflaga.name} {self.mandats} {self.odafim}"
    def incrementOdafim(self):
        self.odafim +=1
        self.modedNext = (self.votes / (self.mandats + 1 + self.odafim))
    def __repr__(self):
        return str(self)

ahuzHashima = 3.25
miflagaList = []
reshimaList = []

def displayMandats(miflagaList, reshimaList, ahuzHashima):
    totalVotes = sum([miflaga.votes for miflaga in miflagaList])
    passingMiflagot = [miflaga for miflaga in miflagaList if (miflaga.votes > totalVotes * ahuzHashima / 100)]
    actualVotes = sum([miflaga.votes for miflaga in passingMiflagot])
    print(totalVotes, passingMiflagot, actualVotes)
    # verify reshimot
    actualReshimaList = [reshima for reshima in reshimaList if (reshima.miflaga in passingMiflagot and reshima.miflaga2 in passingMiflagot)]
    actualReshimaList += [Reshima(miflaga.votes, miflaga, None) for miflaga in passingMiflagot if (miflaga not in [reshima.miflaga for reshima in actualReshimaList] and miflaga not in [reshima.miflaga2 for reshima in actualReshimaList])]
    print(actualReshimaList)
    # parse votes
    modedMandat = actualVotes / 120
    for reshima in actualReshimaList:
        reshima.mandats = floor(reshima.miflaga.votes / modedMandat)
        if (reshima.miflaga2):
            reshima.mandats += floor(reshima.miflaga2.votes / modedMandat)
        reshima.modedNext = (reshima.votes / (reshima.mandats + 1))
    # badder - ofer
    currentMandats = 120 - sum([reshima.mandats for reshima in actualReshimaList])
    while (currentMandats != 0):
        actualReshimaList.sort(key=lambda x: x.modedNext, reverse=True)
        actualReshimaList[0].incrementOdafim()
        currentMandats = 120 - sum([(reshima.mandats + reshima.odafim) for reshima in actualReshimaList])
    print(actualReshimaList)
    # display
    for reshima in actualReshimaList:
        if not (reshima.miflaga2):
            reshima.miflaga.mandats = (reshima.mandats + reshima.odafim)
            print(reshima.miflaga)
        else:
            miflaga1 = reshima.miflaga
            miflaga2 = reshima.miflaga2
            miflaga1.mandats = floor(miflaga1.votes / modedMandat)
            miflaga2.mandats = floor(miflaga2.votes / modedMandat)
            odafim = reshima.odafim
            while (odafim>0):
                moded1 = miflaga1.votes / (miflaga1.mandats + 1)
                moded2 = miflaga2.votes / (miflaga2.mandats + 1)
                if (moded2 > moded1):
                    miflaga2.mandats += 1
                else:
                    miflaga1.mandats += 1
                odafim -= 1
            print(miflaga1)
            print(miflaga2)


            
    







print('1 - add miflagot \n2 - modify odafim \n3 - import miflagot from file\n4 - import reshimot from file\n5 - print inputed miflagot\n6 - display mandats\n7 - end program' )
programEnded = False

while (programEnded==False):
    print('> ', end='')
    command = input()
    if command=='help':
        print('1 - add miflagot \n2 - modify odafim \n3 - import miflagot from file\n4 - import reshimot from file\n5 - print inputed miflagot\n6 - display mandats\n7 - end program' )
    
    elif command == '1':
        while True:
            print("Whats the name of the miflaga? ", end='')
            name = input()
            print("How many votes did it get? ", end='')
            votes = input()
            newMiflaga = Miflaga(votes, name)
            miflagaList.append(newMiflaga)
            print("would you like to quit? (y/n) ", end='')
            toQuit = input()
            if (toQuit == 'y' or toQuit=='yes'):
                break
    
    elif command == '2':
        while True:
            for miflaga in miflagaList:
                print(miflaga)
            print('please choose the first miflaga: ', end='')
            miflaga1name = input()
            print('please choose the second miflaga: ', end='')
            miflaga2name = input()
            for miflaga in miflagaList:
                if miflaga.name == miflaga1name:
                    miflaga1 = miflaga
                if miflaga.name == miflaga2name:
                    miflaga2 = miflaga
            reshimaToAdd = Reshima(miflaga1.votes + miflaga2.votes, miflaga1, miflaga2,None)
            print(reshimaToAdd)
            reshimaList.append(reshimaToAdd)
            print("would you like to quit? (y/n) ", end='')
            toQuit = input()
            if (toQuit == 'y' or toQuit=='yes'):
                break
    elif command == '3':
        f = open('miflagot.txt', 'r', encoding = 'utf-8')
        for line in f.readlines():
            name = line.split(' ')[1][:-1]
            votes = line.split(' ')[0]
            miflagaList.append(Miflaga(votes, name))
    elif command == '4':
        f = open('reshimot.txt', 'r', encoding = 'utf-8')
        for line in f.readlines():
            miflaga2name = line.split(' ')[1][:-1]
            miflaga1name = line.split(' ')[0]
            for miflaga in miflagaList:
                if miflaga.name == miflaga1name:
                    miflaga1 = miflaga
                if miflaga.name == miflaga2name:
                    miflaga2 = miflaga
            reshimaToAdd = Reshima(miflaga1.votes + miflaga2.votes, miflaga1, miflaga2,None)
            reshimaList.append(reshimaToAdd)
    elif command == '5':
        for reshima in reshimaList:
            print(reshima)
        for miflaga in miflagaList:
            print(miflaga)
        
    elif command == '6':
        displayMandats(miflagaList, reshimaList, ahuzHashima)

    elif command == '7':
        programEnded = True
