# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionTanyaIP(Action):

    def name(self) -> Text:
        return "action_tanya_ips_dan_ipk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        for e in entities:
            if e['entity'] == 'ip':
                message = e['value']

        if message == "ips":
            dispatcher.utter_message(text="IPS atau Indeks Prestasi Semester yaitu sistem penilaian yang diterapkan oleh kampus dan hasil penjumlahan semua nilai mata kuliah selama satu semester")
        elif message == "ipk":
            dispatcher.utter_message(text="IPK atau Indeks Prestasi Kumulatif merupakan IPS kumulatif dari seluruh semester yang telah diikuti mahasiswa")
        elif message == "ip":
            dispatcher.utter_message(text="IP atau Indeks Prestasi dibuat sebagai indikator keberhasilan mahasiswa dalam mengikuti kegiatan-kegiatan akademik")
        else:
            dispatcher.utter_message(text="Apakah anda ingin bertanya tentang index prestasi?")

        return []
