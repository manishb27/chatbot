# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetInterest(Action):

    def name(self) -> Text:
        return "action_get_interest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # storing the list of interest extracted from user input
        interst_list =  next(tracker.get_latest_entity_value("interest"), None)

        msg = f'There are your interests? {', '.join(interst_list)}'

        dispatcher.utter_message(text=msg)

        return []
