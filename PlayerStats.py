class PlayerStats():
    def __init__(self):
        self.clear()

    def clear(self):
        self.Name = ""
        self.nationality = ""
        self.team = ""
        self.matches = 0
        self.innings = 0
        # Batting Page
        self.runs = 0
        self.notout = 0
        self.highScore = 0
        self.battingAverage = 0
        self.ballsFaced = 0
        self.battingStrikeRate = 0
        self.Hundreds = 0
        self.Fifties = 0
        self.Fours = 0
        self.Sixes = 0
        # Bowling Page
        self.overs = 0
        self.runsGiven = 0
        self.wickets = 0
        self.bowlingAverage = 0
        self.economy = 0
        self.bowlingStrikeRate = 0
        # Points Page
        self.points = 0

    def SetTeamName(self, teamNo):
        if teamNo == 1:
            self.team = 'CSK'
        elif teamNo == 3:
            self.team = 'DD'
        elif teamNo == 4:
            self.team = 'KXIP'
        elif teamNo == 5:
            self.team = 'KKR'
        elif teamNo == 6:
            self.team = 'MI'
        elif teamNo == 9:
            self.team = 'RCB'
        elif teamNo == 8:
            self.team = 'RR'
        elif teamNo == 62:
            self.team = 'SRH'
        pass


# Global Player List
playerList = []
