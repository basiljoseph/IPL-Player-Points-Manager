import HTMLParser
import copy
from PlayerStats import PlayerStats, playerList


class WicketsData(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.singlePlayer = PlayerStats()
        self.clear()

    def clear(self):
        self.startDataCollection = False
        self.matchesFound = False
        self.inningsFound = False
        self.oversFound = False
        self.runsGivenFound = False
        self.wicketsFound = False
        self.bowlingAverageFound = False
        self.economyFound = False
        self.bowlingStrikeRateFound = False

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
                elif "top-players__ov" in attrs[0][1]:
                    self.oversFound = True
                elif "top-players__r" in attrs[0][1]:
                    self.runsGivenFound = True
                elif "top-players__w" in attrs[0][1]:
                    self.wicketsFound = True
                elif "top-players__a" in attrs[0][1]:
                    self.bowlingAverageFound = True
                elif "top-players__e" in attrs[0][1]:
                    self.economyFound = True
                elif "top-players__sr" in attrs[0][1]:
                    self.bowlingStrikeRateFound = True

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
            elif self.oversFound:
                self.singlePlayer.overs = float(value)
                self.oversFound = False
            elif self.runsGivenFound:
                self.singlePlayer.runsGiven = int(value)
                self.runsGivenFound = False
            elif self.wicketsFound:
                self.singlePlayer.wickets = int(value.replace('*', ''))
                self.wicketsFound = False
            elif self.bowlingAverageFound:
                self.singlePlayer.bowlingAverage = float(value)
                self.bowlingAverageFound = False
            elif self.economyFound:
                self.singlePlayer.economy = float(value)
                self.economyFound = False
            elif self.bowlingStrikeRateFound:
                self.singlePlayer.bowlingStrikeRate = float(value)
                self.bowlingStrikeRateFound = False

    def handle_endtag(self, tag):
        if self.startDataCollection:
            if tag == 'tr':
                player = copy.deepcopy(self.singlePlayer)
                for playerItr in playerList:
                    if playerItr.Name == player.Name:
                        playerItr.overs = copy.deepcopy(player.overs)
                        playerItr.runsGiven = copy.deepcopy(player.runsGiven)
                        playerItr.wickets = copy.deepcopy(player.wickets)
                        playerItr.bowlingAverage = copy.deepcopy(player.bowlingAverage)
                        playerItr.economy = copy.deepcopy(player.economy)
                        playerItr.bowlingStrikeRate = copy.deepcopy(player.bowlingStrikeRate)
                        break
                else:
                    playerList.append(player)
                self.singlePlayer.clear()
                self.clear()
