import requests
import json

stravaUrl = "https://www.strava.com/api/v3"
stravaToken = ''

smartsheetUrl = 'https://api.smartsheet.com/2.0'
smartsheetToken = ''
sheetID = 8914176844976004

headers = {
    "Authorization": f"Bearer {smartsheetToken}",
    "Content-Type": "application/json"
}

activitiesData = []
postData = []

#Call Strava API, loop through activitiesData, and format data to be posted

def getStravaData():

    try:

        stravaActivities = requests.get(f"{stravaUrl}/activities?access_token={stravaToken}")
        stravaActivities.raise_for_status()
        activitiesData = stravaActivities.json()
        print(activitiesData)

        if stravaActivities.status_code == 200:

            for i in activitiesData:
                postData.append( {
                    "cells": [
                        {
                            "columnId": 4384445260582788,
                            "value": i['id']
                        },

                        {
                            "columnId": 8888044887953284,
                            "value": f"{i['start_date']}"
                        },

                        {
                            "columnId": 91951865745284,
                            "value": f"{i['distance']}"
                        },

                        {
                            "columnId": 4595551493115780,
                            "value": f"{i['moving_time']}"
                        }
                    ]
                }
                )

    except requests.exceptions.HTTPError as errHttp:

        print(f"HTTP Error: {errHttp}")

    except requests.exceptions.ConnectionError as errConn:

        print(f"Connection Error: {errConn}")

    except requests.exceptions.Timeout as errTime:

        print(f"Timeout Error: {errTime}")

    
#Post data to Smartsheet

def postStravaToSmartsheet():

    try:

        for i in postData:

            smartsheetResponse = requests.post(f"{smartsheetUrl}/sheets/{sheetID}/rows", headers=headers, json=i)
            smartsheetResponse.raise_for_status()
            print(smartsheetResponse.json())

    except requests.exceptions.HTTPError as errHttp:

        print(f"HTTP Error: {errHttp}")

    except requests.exceptions.ConnectionError as errConn:

        print(f"Connection Error: {errConn}")

    except requests.exceptions.Timeout as errTime:

        print(f"Timeout Error: {errTime}")



getStravaData()
print(postStravaToSmartsheet())





