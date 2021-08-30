# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, Restarted

import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/"

POKEMON_TIPOS = {
    "normal": "normal",
    "fighting": "lucha",
    "flying": "volador",
    "poison": "veneno",
    "ground": "tierra",
    "rock": "roca",
    "bug": "bicho",
    "ghost": "fantasma",
    "steel": "acero",
    "fire": "fuego",
    "water": "agua",
    "grass": "planta",
    "electric": "eléctrico",
    "psychic": "psíquico",
    "ice": "hielo",
    "dragon": "dragón",
    "dark": "siniestro",
    "fairy": "hada"
}

class ActionSearchPokemon(Action):

    def name(self):
        return "action_search_pokemon"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name_pokemon = tracker.get_slot("name_pokemon")
        id_pokemon = tracker.get_slot("id_pokemon")

        if name_pokemon and not id_pokemon:
            req = requests.get(POKEAPI_URL + "pokemon/" + name_pokemon.lower())
        elif id_pokemon and not name_pokemon:
            req = requests.get(POKEAPI_URL + "pokemon/" + id_pokemon)

        if req.status_code == 404:
            dispatcher.utter_message(response="utter_pokemon_no_founded")
            return [AllSlotsReset()]

        info = req.json()
        info_id_pokemon = str(info.get("id"))
        info_name_pokemon = info.get("name").title()
        info_type_pokemon = ", ".join(
            [POKEMON_TIPOS.get(t.get("type").get("name")) for t in info.get("types")])
        info_image_pokemon = info.get("sprites").get("front_default")

        if info_image_pokemon:
            dispatcher.utter_message(
                response="utter_info_pokemon",
                id=info_id_pokemon,
                name=info_name_pokemon,
                type_pokemon=info_type_pokemon,
                image=info_image_pokemon
            )
        else:
            dispatcher.utter_message(
                response="utter_info_pokemon_without_imagen",
                id=info_id_pokemon,
                name=info_name_pokemon,
                type_pokemon=info_type_pokemon
            )
        return [AllSlotsReset()]
