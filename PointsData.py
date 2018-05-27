import HTMLParser
import copy
from PlayerStats import PlayerStats, playerList


class PointsData(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.singlePlayer = PlayerStats()
        self.clear()

    def clear(self):
        self.startDataCollection = False
        self.pointsFound = False

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            if "js-row" in attrs[0][1]:
                self.startDataCollection = True
                return

        if self.startDataCollection:
            if tag == 'img':
                if "Headshot" in attrs[2][1]:
                    self.singlePlayer.Name = attrs[2][1].replace(' Headshot', '')
            elif tag == 'td':
                if "top-players__pts" in attrs[0][1]:
                    self.pointsFound = True

    def handle_data(self, data):
        if self.startDataCollection:
            value = data.replace('\n', '').replace(' ', '')
            if value == '-':
                value = 0
            if self.pointsFound:
                self.singlePlayer.points = float(value)
                self.pointsFound = False

    def handle_endtag(self, tag):
        if self.startDataCollection:
            if tag == 'tr':
                player = copy.deepcopy(self.singlePlayer)
                for playerItr in playerList:
                    if playerItr.Name == player.Name:
                        playerItr.points = copy.deepcopy(player.points)
                        break
                else:
                    playerList.append(player)
                self.singlePlayer.clear()
                self.clear()
