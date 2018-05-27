import HTMLParser
import copy
from PlayerStats import PlayerStats, playerList


class RunsData(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.singlePlayer = PlayerStats()
        self.clear()

    def clear(self):
        self.startDataCollection = False
        self.matchesFound = False
        self.inningsFound = False
        self.runsFound = False
        self.notoutFound = False
        self.highScoreFound = False
        self.averageFound = False
        self.ballsFacedFound = False
        self.strikeRateFound = False
        self.HundredsFound = False
        self.FiftiesFound = False
        self.FoursFound = False
        self.SixesFound = False
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            if "js-row" in attrs[0][1]:
                self.startDataCollection = True
                self.singlePlayer.nationality = attrs[1][1]
                self.singlePlayer.SetTeamName(int(attrs[2][1]))
                return

        if self.startDataCollection:
            if tag == 'img':
                if "Headshot" in attrs[2][1]:
                    self.singlePlayer.Name = attrs[2][1].replace(' Headshot', '')
            elif tag == 'td':
                if "top-players__m" in attrs[0][1]:
                    self.matchesFound = True
                elif "top-players__inns" in attrs[0][1]:
                    self.inningsFound = True
                elif "top-players__r" in attrs[0][1]:
                    self.runsFound = True
                elif "top-players__no" in attrs[0][1]:
                    self.notoutFound = True
                elif "top-players__hs" in attrs[0][1]:
                    self.highScoreFound = True
                elif "top-players__a" in attrs[0][1]:
                    self.averageFound = True
                elif "top-players__b" in attrs[0][1]:
                    self.ballsFacedFound = True
                elif "top-players__sr" in attrs[0][1]:
                    self.strikeRateFound = True
                elif "top-players__100s" in attrs[0][1]:
                    self.HundredsFound = True
                elif "top-players__50s" in attrs[0][1]:
                    self.FiftiesFound = True
                elif "top-players__4s" in attrs[0][1]:
                    self.FoursFound = True
                elif "top-players__6s" in attrs[0][1]:
                    self.SixesFound = True

    def handle_data(self, data):
        if self.startDataCollection:
            value = data.replace('\n', '').replace(' ', '')
            if value == '-':
                value = 0
            if self.matchesFound:
                self.singlePlayer.matches = int(value)
                self.matchesFound = False
            elif self.inningsFound:
                self.singlePlayer.innings = int(value)
                self.inningsFound = False
            elif self.inningsFound:
                self.singlePlayer.innings = int(value)
                self.inningsFound = False
            elif self.runsFound:
                self.singlePlayer.runs = int(value)
                self.runsFound = False
            elif self.notoutFound:
                self.singlePlayer.notout = int(value)
                self.notoutFound = False
            elif self.highScoreFound:
                self.singlePlayer.highScore = int(value.replace('*', ''))
                self.highScoreFound = False
            elif self.averageFound:
                self.singlePlayer.battingAverage = float(value)
                self.averageFound = False
            elif self.ballsFacedFound:
                self.singlePlayer.ballsFaced = int(value)
                self.ballsFacedFound = False
            elif self.strikeRateFound:
                self.singlePlayer.battingStrikeRate = float(value)
                self.strikeRateFound = False
            elif self.HundredsFound:
                self.singlePlayer.Hundreds = int(value)
                self.HundredsFound = False
            elif self.FiftiesFound:
                self.singlePlayer.Fifties = int(value)
                self.FiftiesFound = False
            elif self.FoursFound:
                self.singlePlayer.Fours = int(value)
                self.FoursFound = False
            elif self.SixesFound:
                self.singlePlayer.Sixes = int(value)
                self.SixesFound = False

    def handle_endtag(self, tag):
        if self.startDataCollection:
            if tag == 'tr':
                player = copy.deepcopy(self.singlePlayer)
                playerList.append(player)
                self.singlePlayer.clear()
                self.clear()
