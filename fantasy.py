import RunsData
import WicketsData
import PointsData
import imp
import os
import urllib
from PlayerStats import playerList


def module_missing(module_name):
    print "Cannot find " + module_name + " module"
    print "Please download " + module_name + " module first"
    os.system('pause')
    exit()


# Check whether all the necessary modules are installed
try:
    imp.find_module('openpyxl')
    import openpyxl
except:
    module_missing('openpyxl')


def as_text(value):
    if value is None:
        return ""
    return str(value)


def save_data():
    wb = openpyxl.load_workbook("data.xlsx")
    sheet = wb['Sheet1']

    sheet['A1'] = 'Name'
    sheet['B1'] = 'Team'
    sheet['C1'] = 'Nationality'
    sheet['D1'] = 'Matches'
    sheet['E1'] = 'Innings'
    sheet['F1'] = 'Runs'
    sheet['G1'] = 'Not Out'
    sheet['H1'] = 'High Score'
    sheet['I1'] = 'Batting Average'
    sheet['J1'] = 'Balls Faced'
    sheet['K1'] = 'Strike Rate'
    sheet['L1'] = 'Hundreds'
    sheet['M1'] = 'Fifties'
    sheet['N1'] = 'Fours'
    sheet['O1'] = 'Sixes'
    sheet['P1'] = 'Overs'
    sheet['Q1'] = 'Runs Given'
    sheet['R1'] = 'Wickets'
    sheet['S1'] = 'Bowling Average'
    sheet['T1'] = 'Economy'
    sheet['U1'] = 'Bowling Strike Rate'
    sheet['V1'] = 'IPL Points'

    for idx in range(len(playerList)):
        sheet['A' + str(idx + 2)] = playerList[idx].Name
        sheet['B' + str(idx + 2)] = playerList[idx].team
        sheet['C' + str(idx + 2)] = playerList[idx].nationality
        sheet['D' + str(idx + 2)] = playerList[idx].matches
        sheet['E' + str(idx + 2)] = playerList[idx].innings
        sheet['F' + str(idx + 2)] = playerList[idx].runs
        sheet['G' + str(idx + 2)] = playerList[idx].notout
        sheet['H' + str(idx + 2)] = playerList[idx].highScore
        sheet['I' + str(idx + 2)] = playerList[idx].battingAverage
        sheet['J' + str(idx + 2)] = playerList[idx].ballsFaced
        sheet['K' + str(idx + 2)] = playerList[idx].battingStrikeRate
        sheet['L' + str(idx + 2)] = playerList[idx].Hundreds
        sheet['M' + str(idx + 2)] = playerList[idx].Fifties
        sheet['N' + str(idx + 2)] = playerList[idx].Fours
        sheet['O' + str(idx + 2)] = playerList[idx].Sixes
        sheet['P' + str(idx + 2)] = playerList[idx].overs
        sheet['Q' + str(idx + 2)] = playerList[idx].runsGiven
        sheet['R' + str(idx + 2)] = playerList[idx].wickets
        sheet['S' + str(idx + 2)] = playerList[idx].bowlingAverage
        sheet['T' + str(idx + 2)] = playerList[idx].economy
        sheet['U' + str(idx + 2)] = playerList[idx].bowlingStrikeRate
        sheet['V' + str(idx + 2)] = playerList[idx].points

    # Freeze the top row and first two columns
    sheet.freeze_panes = 'C2'

    # Adjust Column Length
    for columnItr in sheet.columns:
        length = max(len(as_text(cell.value)) for cell in columnItr)
        sheet.column_dimensions[columnItr[0].column].width = length + 1

    wb.save("data.xlsx")


def main():
    opener = urllib.FancyURLopener({})

    runs = RunsData.RunsData()
    runs.feed(opener.open("https://www.iplt20.com/stats/2018/most-runs").read())

    wickets = WicketsData.WicketsData()
    wickets.feed(opener.open("https://www.iplt20.com/stats/2018/most-wickets").read())

    points = PointsData.PointsData()
    points.feed(opener.open("https://www.iplt20.com/stats/2018/player-points").read())

    # Save all the data
    save_data()


if __name__ == '__main__':
    main()
