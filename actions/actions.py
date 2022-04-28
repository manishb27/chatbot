from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

ML = 'Machine learning is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence.'


DL = 'Deep learning is a machine learning technique that teaches computers to do what comes naturally to humans: learn by example. Deep learning is a key technology behind driverless cars, enabling them to recognize a stop sign, or to distinguish a pedestrian from a lamppost.'

DB = 'A dashboard is a type of graphical user interface which often provides at-a-glance views of key performance indicators (KPIs) relevant to a particular objective or business process. In other usage, "dashboard" is another name for "progress report" or "report" and considered a form of data visualization. In providing this overview, business owners can save time and improve their decision making by utilizing dashboards.'

DE = 'Data engineering is the complex task of making raw data usable to data scientists and groups within an organization. Data engineering encompasses numerous specialties of data science.'

AI = 'Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals.'

class ActionGetInterest(Action):

    def name(self) -> Text:
        return "action_get_interest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # storing the list of interest extracted from user input
        interst_list =  (tracker.get_slot("interests"))

        # starting loop if tracker finds a list in the slots
        if interst_list != []:

            # looping over the interst_list
            for interest in interst_list:
                
                # priting machine learning message
                if interest = Machine Learning:
                    msg = ML
                    dispatcher.utter_message(text=msg)

                # pringint deep learning message
                elif interest = Deep Learning:
                    msg = DL
                    dispatcher.utter_message(text=msg)

                #  printing Data engg message
                elif interest = Data Engineering:
                    msg = DE
                    dispatcher.utter_message(text=msg)

                # printing dash board message
                elif interest = Data Visualization & Dash Boards:
                    msg = DB
                    dispatcher.utter_message(text=msg)

                # printing AI message
                elif interest = Arificial Intelligence
                    msg = AI
                    dispatcher.utter_message(text=msg)




        # msg = f'There are your interests? {interst_list}'

        # dispatcher.utter_message(text=msg)

        return []
