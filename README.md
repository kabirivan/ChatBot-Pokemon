# ChatBot-Pokemon

## Create a Pokémon chatbot in Spanish with RASA
The objective will be to develop a chatbot that allows the user to search for information about any Pokémon, providing its name.
[<img src="images/pokemon.png" width="600"/>](images/pokemon.png)

### How will the chatbot know what to look for?
Somehow we need to store the name of the Pokémon to search to be able to use it in the PokéApi. RASA supports Entity Recognition methods, which will be useful for this task.


## Update Rasa
pip install rasa --upgrade

## Create Virtual Environment 
python3 -m venv env
source env/bin/activate
