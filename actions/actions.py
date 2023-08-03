# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class GetWeather(Action):
        def name(self) -> Text:
                return "action_check_weather"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            current_place=next(tracker.get_latest_entity_values ("location"), None)
            #msg=f"{tracker.latest_message}"
            #dispatcher.utter_message(text=msg)
       
          
            #if current_place is "is" or "Is" or "give" or "give":
                   #current_place=tracker.latest_message['entities'][1]['value']
                   #For_testing branch action

                  #start here. it was stopped at this position. extracting 2nd entity from the list

            error_msg_CP_None=f"Current Place is None from Lookup table, Sorry, such a location {current_place} could not be found in the database. Can you recheck and enter the location correctly again?" 
            error_msg_COD_200=f"Error !=200, Sorry, such a location {current_place} could not be found in the database. Can you recheck and enter the location correctly again?" 

            if current_place is None:
                   dispatcher.utter_message(text=error_msg_CP_None) 
                   return[]

            elif current_place is not None:
                   url="https://api.openweathermap.org/data/2.5/weather?q="+current_place+"&units=metric&APPID=feaa6c93d5751b9d4c9a8ab314ac10af"
                   response=requests.get(url)
                   data=response.json()

                   if(int(data['cod'])!=200):
                          dispatcher.utter_message(text=error_msg_COD_200) 
                   else:
                          msg=f"Weather at {current_place} is {data['main']}, code is {data['cod']}. "
                          dispatcher.utter_message(text=msg)
              
