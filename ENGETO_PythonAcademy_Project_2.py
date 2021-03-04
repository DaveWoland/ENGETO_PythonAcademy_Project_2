
from random import choice

def main():
    text0 = "I've generated a random 4 digits number for you."
    text1 = "Let's play a bulls and cows game."

    print("Hi there!")
    oddelovac(text0)
    print(text0)
    print(text1)
    oddelovac(text0)

    #Vygenerovani 4 cislic
    lst_4 = random_4()

    #Vyhodnoceni tipu uzivatele
    tipovani = True
    while tipovani:

        # Vstup a kontrola vstupu uzivatele
        player_input_string = vstup_kontrola()

        #Prevod vstupu uzivatele na list cisel
        player_input_lst = vstup_prevod(player_input_string)

        if player_input_lst == lst_4:
            print(f"Correct, you've guessed the right number.")
            exit()
        else:
            bull_cow(player_input_lst, lst_4)



def oddelovac(text):
    print(len(text) * "-")


#def fce generovani 4 cisel (zadne se neopakuje, prvni nesmi byt 0)
def random_4():
    lst_random_4 = []
    no_lst = [0,1,2,3,4,5,6,7,8,9]

    #Vyber prniho cisla, aby nebylo "0". Odstraneni cisla, aby se neopakovalo.
    first = choice(no_lst[1:])
    lst_random_4.append(first)
    no_lst.remove(first)

    #Vyber zbylych cisel. Po kazdem vyberu odstraneni, aby se neopakovala.
    for x in range(3):
        number = choice(no_lst)
        lst_random_4.append(number)
        no_lst.remove(number)

    return lst_random_4


#def fce vstup a kontrola hracem zadaneho cisla, ze je presne 4 znaky, znaky jsou cisla a prvni neni 0
def vstup_kontrola():
    kontrola = True
    while kontrola:
        player_input = input("Enter a number: ")
        if len(player_input) != 4 or player_input[0] == '0' or not player_input.isdigit() or len(set(player_input)) != 4:
            continue
        else:
            kontrola = False

    return player_input

#def fce prevedeni uzivatelova vstupu (stringu) na list cisel
def vstup_prevod(string):
    lst_vstup = []
    for char in string:
        lst_vstup.append(int(char))
    return lst_vstup

#def fce kontrola shody cisel a umisteni, kontrola poctu spravnych cisel
def bull_cow(player, game_no):
    player_no = list(player)
    spravna_pozice = 0
    spravne_cislo = 0
    byk = ['bulls', 'bull']
    krava = ['cows', 'cow']

    for i, x in enumerate(player_no):
        for j, y in enumerate(game_no):
            if x == y and i == j:
                spravna_pozice += 1
                break
            elif x == y:
                spravne_cislo += 1
                break

    vystup = [f"{spravna_pozice} {byk[spravna_pozice == 1]}, {spravne_cislo} {krava[spravne_cislo == 1]}"]
    print(vystup)

main()
#def casu hry

#def poctu odhadu

#opravit popisky parametru

#Dopsat info o proměnných k definovaným funkcím