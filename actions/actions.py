from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from re import search
import boto3
from botocore.exceptions import ClientError


class ActionCreateUserRole(Action):

    def name(self) -> Text:
        return "action_create_user_role"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get("entities", [])
        
        sender_id = tracker.sender_id

        substring = "admin"
        substring2 = "dev"
        if search(substring, sender_id):
            #admin
            if not entities:
                dispatcher.utter_message(text="Please enter the IAM user name")
            else:
                # Set your AWS credentials
                AWS_ACCESS_KEY_ID = 'AKIA6CXDF6RZTV3CBL4L'
                AWS_SECRET_ACCESS_KEY = 'pVsxfrPtTE/E7tRBlJcgSrqVrpo+78qHXH9AXsD9'
                client = boto3.client('iam', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
                user_name = entities[0]['value']
               
                try:
                    response = client.create_user(UserName=user_name)
                    print(f"IAM user '{user_name}' created successfully.")
                    dispatcher.utter_message(text=f"IAM user '{user_name}' created successfully.")
               
                except ClientError as e:
                    print(e)
                
        
        elif search(substring2, sender_id):
             #developer

            if not entities:
                dispatcher.utter_message(text="Please enter the IAM user name")
            else:
                AWS_ACCESS_KEY_ID = 'AKIA6CXDF6RZXXH7KEW6'
                AWS_SECRET_ACCESS_KEY = '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'
                user_name = entities[0]['value']
    
                try:
                    client = boto3.client('iam', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
                    response = client.create_user(UserName=user_name)
                    print(response)
                    
               
                except ClientError as e:
                    dispatcher.utter_message(text=str(e))


        else:
            print("error determining the user type")


        return []
