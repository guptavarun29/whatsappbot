import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "jokes-ahlyrh-88881a73d59b.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "jokes-ahlyrh"