import requests
import functools
import random

base_url = "https://swapi.dev/api/people/"

def get_swapi_info(number):
    url = f"{base_url}/{number}"
    response = requests.get(url)

    if response.status_code == 200:
        person_data = response.json()
        return person_data
    else:
        print(f"Info Request Could Not Be Recieved {response}")

def get_swapi_count():
    url = base_url
    response = requests.get(url)

    if response.status_code == 200:
        person_data = response.json()
        return person_data
    else:
        print(f"Count Request Could Not Be Recieved {response}")

def swapi_compare(swapi, trait, player, computer):
    player_choice = swapi['results'][player][trait]
    computer_choice = swapi['results'][computer][trait]

    if isinstance(player_choice, list) == True and isinstance(computer_choice, list) == True:
        player_amount = len(player_choice)
        computer_amount = len(computer_choice)

        if player_amount > computer_amount:
            return 0
        elif computer_amount > player_amount:
            return 1
        else:
            return 2
    else:
        if player_choice > computer_choice:
            return 0
        elif computer_choice > player_choice:
            return 1
        else:
            return 2

    


def main():

    swapi_count = len(get_swapi_count())
    swapi_people = get_swapi_count()
     
    for i in range(len(swapi_people['results'])):
        print(f"[{i}] {swapi_people['results'][i]['name']}")

    
    swapi_player_choice = int(input('Make Your Choice!'))
    swapi_computer_choice = random.randint(0, len(swapi_people['results']))

    print('Select The Trait You\'ll Be Comparing:\n[0] Height\n[1] Mass\n[2] # of Films\n[3] # of Starships Piloted\n[4] # of Vehicles Piloted')

    swapi_trait_choice = int(input())

    if swapi_trait_choice == 0:
        swapi_compare(swapi_people, 'height', swapi_player_choice, swapi_computer_choice)
    elif swapi_trait_choice == 1:
        swapi_compare(swapi_people, 'mass', swapi_player_choice, swapi_computer_choice)
    elif swapi_trait_choice == 2:
        swapi_compare(swapi_people, 'films', swapi_player_choice, swapi_computer_choice)
    elif swapi_trait_choice == 3:
        swapi_compare(swapi_people, 'starships', swapi_player_choice, swapi_computer_choice)
    elif swapi_trait_choice == 4:
        swapi_compare(swapi_people, 'vehicles', swapi_player_choice, swapi_computer_choice)
    else:
        pass


if __name__ == "__main__":
    main()

