# Implement Client Script and UI Policy (Incident)

This project demonstrates Client Script and UI Policy behavior for the ServiceNow Incident topic.

Client Script:
- Category = Software -> Priority = 2 - High
- Category = Hardware -> Priority = 3 - Moderate
- On submit, Caller and Description are required.

UI Policy:
- State = In Progress -> Description becomes mandatory.
- State = Closed -> Priority is hidden.

Run:
1. pip install -r requirements.txt
2. python app.py
3. Open the address shown in the terminal.

The `servicenow_scripts` folder contains ServiceNow-style scripts and the `docs` folder contains implementation steps and test cases.
