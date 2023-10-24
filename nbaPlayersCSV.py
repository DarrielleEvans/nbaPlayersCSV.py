import json
import requests
import os
import csv



# fetch the data using a get request
url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
	"X-RapidAPI-Key": "5678679871msh0a8eb106a65e205p16d113jsn6d7f4f50ec42",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#store the json response in a variable
playerList = response.json()
#store the total number of pages that have NBA player information as a variable
pages = playerList['meta']['total_pages']
#store the length of the player list per page
totalData = len(playerList['data'])

#create a function that will make the csv file
def makeCSV():

#header names for the csv file
    fieldnames = ['Player ID', 'First Name', 'Last Name', 'Position', 'Team Name' ]
    rows = []

# create a nested for loop that will iterate through the list of players per page
    for page in range(0, pages):
        playerList['meta']['current_page'] = page

        for i in range(0, totalData):
                rows.append({'Player ID':playerList['data'][i]['id'], 
            'First Name':playerList['data'][i]['first_name'], 
            'Last Name':playerList['data'][i]['last_name'],
            'Position':playerList['data'][i]['position'],
            'Team Name':playerList['data'][i]['team']['name']
            })
# create csv file with data appended to each row
        with open('nba.csv', 'a', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if page == 0:
                writer.writeheader()
            writer.writerows(rows)
    print("CSV Created")

makeCSV()
