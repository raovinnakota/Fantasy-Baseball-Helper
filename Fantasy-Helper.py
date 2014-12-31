################################
import csv
import operator
################################

fileName = 'Final Project Players - Sheet1.csv'
positionList = ['C','1B','2B','3B','SS','LF','CF','RF','DH']

################################

class Fantasy_Player(object):
    def __init__(self):
        self.requestType = None
        self.leaderboards = Leaderboards()
        
    def setRequestType(self):
        self.requestType = raw_input('''Welcome to the draft helper! What would you like to do? Your choices are:
        look at the leaderboards or see a mock draft''')
    
    def choiceResults(self):
        self.setRequestType()
        if self.requestType == 'look at the leaderboards':
            answer = raw_input("Which position do you want to see?")
            if answer == 'catcher' or answer == 'Catcher' or answer =='C':
                self.leaderboards.printBestCatchers()
            elif answer == 'first base' or answer == 'First Base' or answer == '1st Base' or answer == '1B' or answer == '1b':
                self.leaderboards.printBestFirstBasemen()
            elif answer == 'second base' or answer == 'Second Base' or answer == '2nd Base' or answer == '2B' or answer == '2b':
                self.leaderboards.printBestSecondBasemen()
            elif answer == 'third base' or answer == 'Third Base' or answer == '3rd Base' or answer == '3B' or '3b':
                self.leaderboards.printBestThirdBasemen()
            elif answer == 'shortstop' or answer == 'Shortstop' or answer == 'SS':
                self.leaderboards.printBestShortStop()
            elif answer == 'left field' or answer == 'Left Field' or answer == 'LF':
                self.leaderboards.printBestLeftFielder()
            elif answer == 'center field' or answer == 'Center Field' or answer == 'CF':
                self.leaderboards.printBestCenterFielder()
            elif answer == 'right field' or answer == 'Right Field' or answer == 'RF':
                self.leaderboards.printBestRightFielder()
        elif self.requestType == 'see a mock draft':
            MyDraft = Mock_Draft()
            MyDraft.mockDraft()
            MyDraft.printFantasyTeam1
            MyDraft.printFantasyTeam2
            MyDraft.printFantasyTeam3
            
class DraftIO(object):
    def __init__(self):
        self.draftList = []
    
    def loadPlayers(self):
        f = open(fileName, 'rt')
        try:
            reader = csv.reader(f)
            reader.next()
            for row in reader:
                newPlayer = Player()
                newPlayer.position = row[0]
                newPlayer.name = row[1]
                newPlayer.opsPlus = int(row[2])
                self.draftList.append(newPlayer)
        finally:
            f.close()
        
    def getDraftList(self):
        return self.draftList

class Rankings(object):
    def __init__(self):
        self.rankList = []
        self.draftList = []
    
    def getDraftList(self):
        return self.draftList
    
    def setDraftList(self):
        myDraft = DraftIO()
        myDraft.loadPlayers()
        self.draftList = myDraft.getDraftList()
        
    def setRankList(self):
        self.setDraftList()
        self.getDraftList()
        maxOPS = 0
        bestPlayer = None
        for player in self.draftList:
            self.rankList.append(player)
        self.rankList.sort(key=operator.attrgetter("opsPlus"), reverse = True)
        return self.rankList

class Leaderboards(object):
    def __init__(self):
        self.catchers = []
        self.firstBasemen = []
        self.secondBasemen = []
        self.thirdBasemen = []
        self.shortStop = []
        self.leftField = []
        self.centerField = []
        self.rightField = []
        self.draftList = []
        
    def getDraftList(self):
        return self.draftList
    
    def setDraftList(self):
        MyDraftIO = DraftIO()
        MyDraftIO.loadPlayers()
        self.draftList = MyDraftIO.getDraftList()
    
    def getBestCatchers(self):
        self.setDraftList()
        self.getDraftList()
        #print(self.draftList)
        for player in self.draftList:
            if player.position == 'C':
                self.catchers.append(player)
        self.catchers.sort(key = operator.attrgetter("opsPlus"), reverse = True)
        return self.catchers
        
    def printBestCatchers(self):
        bestCatchers = self.getBestCatchers()
        for player in self.catchers:
            print (player.name, player.opsPlus)
        
    def getBestFirstBasemen(self):
        self.setDraftList()
        self.getDraftList()
        for player in self.draftList:
            if player.position == '1B':
                self.firstBasemen.append(player)
        self.firstBasemen.sort(key = operator.attrgetter("opsPlus"), reverse = True)
        return self.firstBasemen
    
    def printBestFirstBasemen(self):
        self.getBestFirstBasemen()
        for player in self.firstBasemen:
            print(player.name, player.opsPlus)
        
    def getBestSecondBasemen(self):
        self.setDraftList()
        self.getDraftList()
        for player in self.draftList:
            if player.position == '2B':
                self.secondBasemen.append(player)
        self.secondBasemen.sort(key = operator.attrgetter("opsPlus"), reverse = True)
        return self.secondBasemen
        
    def printBestSecondBasemen(self):
        self.getBestSecondBasemen()
        for player in self.secondBasemen:
            print(player.name, player.opsPlus)
        
    def getBestThirdBasemen(self):
        self.setDraftList()
        self.getDraftList()
        for player in self.draftList:
            if player.position == '3B':
                self.thirdBasemen.append(player)
        self.thirdBasemen.sort(key = operator.attrgetter("opsPlus"), reverse = True)
        return self.thirdBasemen
        
    def printBestThirdBasemen(self):
        self.getBestThirdBasemen()
        for player in self.thirdBasemen:
            print(player.name, player.opsPlus)
            
    def getBestShortStop(self):
        self.setDraftList()
        self.getDraftList()
        for player in self.draftList:
            if player.position == 'SS':
                self.shortStop.append(player)
        self.shortStop.sort(key = operator.attrgetter("opsPlus"), reverse = True)
        return self.shortStop
    
    def printBestShortStop(self):
        self.getBestShortStop()
        for ss in self.shortStop:
            print(ss.name, ss.opsPlus)
            
    def getBestLeftFielder(self):
        self.setDraftList()
        self.getDraftList()
        for player in self.draftList:
            if player.position == 'LF':
                self.leftField.append(player)
        self.leftField.sort(key = operator.attrgetter("opsPlus"), reverse = True)
        return self.leftField
    
    def printBestLeftFielder(self):
        self.getBestLeftFielder()
        for lf in self.leftField:
            print(lf.name, lf.opsPlus)
            
    def getBestCenterFielder(self):
        self.setDraftList()
        self.getDraftList()
        for player in self.draftList:
            if player.position == 'CF':
                self.centerField.append(player)
        self.centerField.sort(key = operator.attrgetter("opsPlus"), reverse = True) 
        return self.centerField
    
    def printBestCenterFielder(self):
        self.getBestCenterFielder()
        for cf in self.centerField:
            print(cf.name, cf.opsPlus)
            
    def getBestRightFielder(self):
        self.setDraftList()
        self.getDraftList()
        for player in self.draftList:
            if player.position == 'RF':
                self.rightField.append(player)
        self.rightField.sort(key = operator.attrgetter("opsPlus"), reverse = True)           
        return self.rightField
    
    def printBestRightFielder(self):
        self.getBestRightFielder()
        for rf in self.rightField:
            print(rf.name, rf.opsPlus)
            
class Mock_Draft(object):
    def __init__(self):
        self.rounds = 18
        self.fantasyTeam1 = []
        self.fantasyTeam2 = []
        self.fantasyTeam3 = []
        self.fantasyTeam4 = []
        self.positionList1 = []
        self.positionList2 = []
        self.positionList3 = []
        self.positionList4 = []
        self.rankList = []
        self.ourDraftList = []
        self.draftRound = 9
        
    def getRankList(self): 
        return self.rankList
    
    def setRankList(self):
        myRankings = Rankings()
        myRankings.setRankList()
        self.rankList = myRankings.setRankList()
        
    def mockDraft(self):
        self.setRankList()
        self.getRankList()
        for player in self.rankList:
            self.ourDraftList.append(player)
        while self.draftRound > 0:
            if self.ourDraftList[0].position not in self.positionList1:
                self.fantasyTeam1.append(self.ourDraftList[0])
                self.positionList1.append(self.ourDraftList[0].position)
                self.ourDraftList.pop(0)
            if self.ourDraftList[0].position in self.positionList1:
                for player in self.ourDraftList:
                    if player.position not in self.positionList1:
                        self.fantasyTeam1.append(player)
                        self.positionList1.append(player.position)
                        self.ourDraftList.remove(player)
                        break
            if self.ourDraftList[0].position not in self.positionList2:
                self.fantasyTeam2.append(self.ourDraftList[0])
                self.positionList2.append(self.ourDraftList[0].position)
                self.ourDraftList.pop(0)
            if self.ourDraftList[0].position in self.positionList2:
                for player in self.ourDraftList:
                    if player.position not in self.positionList2:
                        self.fantasyTeam2.append(player)
                        self.positionList2.append(player.position)
                        self.ourDraftList.remove(player)
                        break
            if self.ourDraftList[0].position not in self.positionList3:
                self.fantasyTeam3.append(self.ourDraftList[0])
                self.positionList3.append(self.ourDraftList[0].position)
                self.ourDraftList.pop(0)
            if self.ourDraftList[0].position in self.positionList3:
                for player in self.ourDraftList:
                    if player.position not in self.positionList3:
                        self.fantasyTeam3.append(player)
                        self.positionList3.append(player.position)
                        self.ourDraftList.remove(player)
                        break
            if self.ourDraftList[0].position not in self.positionList4:
                self.fantasyTeam4.append(self.ourDraftList[0])
                self.positionList4.append(self.ourDraftList[0].position)
                self.ourDraftList.pop(0)
            if self.ourDraftList[0].position in self.positionList4:
                for player in self.ourDraftList:
                    if player.position not in self.positionList4:
                        self.fantasyTeam4.append(player)
                        self.fantasyTeam4.append(player.position)
                        self.ourDraftList.remove(player)
                        break
            self.draftRound = self.draftRound - 1
        return (self.fantasyTeam1, self.fantasyTeam2, self.fantasyTeam3, self.fantasyTeam4)
        
    def printFantasyTeam1(self):
        self.mockDraft()
        print("Here's the Team with the 1st Pick")
        for member in self.fantasyTeam1:
            print(member.name, member.position, member.opsPlus)
        
    def printFantasyTeam2(self):
        self.mockDraft()
        print("Here's the Team with the 2nd Pick")
        for member in self.fantasyTeam2:
            print(member.name, member.position, member.opsPlus)
    
    def printFantasyTeam3(self):
        self.mockDraft()
        print("Here's the Team with the 3rd Pick")
        for member in self.fantasyTeam3:
            print(member.name, member.position, member.opsPlus)
    
    def printFantasyTeam4(self):
        self.mockDraft()
        print("Here's the Team with the Last Pick")
        for member in self.fantasyTeam4:
            print(member.name, member.position, member.opsPlus)
         

class Teams_In_League(object):
    def __init__(self):
        self.draft = The_Draft()
        self.fantasyTeam1 = []
        self.fantasyTeam2 = []
        self.fantasyTeam3 = []
        self.fantasyTeam4 = []            


class Player(object):
    def __init__(self):
        self.name = None
        self.position = None
        self.opsPlus = 0

def main():
    MyPlayer = Fantasy_Player()
    MyPlayer.choiceResults()
    #MyLeaderboards = Leaderboards()
    #MyLeaderboards.printBestCatchers()
    
    

if __name__ == "__main__":
    main()
