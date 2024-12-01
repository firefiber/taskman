import sys
import os
import json
import isodate

from datetime import datetime
from pathlib import Path

# Store input commands and available functions
inputCommands = sys.argv[1::]

inputTask = inputCommands[0]
inputFunction = inputCommands[1]

availableFunctions = ['start', 'stop', 'pause', 'edit']

def createTask():
    return {
        "parentTask": None,
        "subTasks":[],
        "startDate": datetime.now().isoformat(),
        "endDate": None,
        "sessions":[],
        "totalDuration": 0,
        "done": False
    }

def createSession():
    return {
        "start": datetime.now().isoformat(),
        "end": None,
        "duration": 0,
        "cleanStop": False
    }

def updateSession(session, fieldToUpdate, valueToUpdate):
    print(session[fieldToUpdate])

if inputFunction in availableFunctions:
    
    if not os.path.isfile('db.json'):
        with open('db.json', 'w') as db:
            data = {"tasks":{}}
            json.dump(data, db)
    
    if inputFunction == 'start':
        with open('db.json', 'r') as db:
            data = json.load(db)

        if inputTask not in data["tasks"].keys():
            newTask = createTask()
            newTask["sessions"].append(createSession())

            data["tasks"][inputTask] = newTask 

            with open('db.json', 'w') as db:
                json.dump(data, db, indent=4)
            
            
    if inputFunction == 'stop':
        with open('db.json', 'r') as db:
            data = json.load(db)

        task = data["tasks"][inputTask]
        sessions = task["sessions"]
        activeSessionID = len(sessions)-1
        activeSession = sessions[activeSessionID] 

        start = activeSession["start"]
        end = datetime.now().isoformat()
        duration = datetime.fromisoformat(end) - datetime.fromisoformat(start)
        durationFormatted = isodate.duration_isoformat(duration)
        
        updatedSession = {
            "start": start,
            "end": end, 
            "duration": durationFormatted,
            "manuallyStopped": True
        }

        session = updatedSession
        task["sessions"][activeSessionID] = session
        data["tasks"][inputTask] = task

        with open('db.json', 'w') as db:
            json.dump(data, db, indent=4)
    # If inputFunction == 'stop':
        # If task name exists:
            # set session stop time
            # set session manual stop flag True
    # If command == 'start'
        # Create new line in db with task name, and timestamp under start column
    
    # If command == 'stop'
        # Enter timestamp under stop column
        # Calculate duration
        # store duration under duration column
        # store duration under duration column


