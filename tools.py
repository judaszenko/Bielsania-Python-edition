import time
import os
clear = lambda: os.system('cls') #pozwala na używanie komendy clear()

hud = 'on' #definiuje czy hud powinien być włączony
lang = 'pl' #język

def hub(): #jeżeli hud='on', wyświetla statystyki na górze każdej strony
    global hud
    global hp, kev, dmg, cash
    clear()
    if (hud == 'on'):
        print("       HP: "+str(hp)+"     DMG: "+str(dmg)+"     KEV:"+str(kev)+"     $: "+str(cash)+" ")
        print(" ⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻")

def intro(): #wyświetla logo gry
    print(" ____________________________________________")
    time.sleep(0.03)
    print(" |  ____         _                 _        |")
    time.sleep(0.03)
    print(" | |  _ \\(_)    | |               (_)       |")
    time.sleep(0.03)
    print(" | | |_) |_  ___| |___  __ _ _ __  _  __ _  |")
    time.sleep(0.03)
    print(" | |  _ <| |/ _ \\ / __|/ _` | '_ \\| |/ _` | |")
    time.sleep(0.03)
    print(" | | |_) | |  __/ \\__ \\ (_| | | | | | (_| | |")
    time.sleep(0.03)
    print(" | |____/|_|\\___|_|___/\\__,_|_| |_|_|\\__,_| |")
    time.sleep(0.03)
    print(" ____________________________________________")

def menu(): #głowne menu, pokazane na początku gry, w późniejszych wersjach ma być widoczne w dowonlym momencie, jeżeli user wprowadzi 0 w czasie ktoregokolwiek dialogu, będzie to służyć jako pauza
    clear()
    intro()
    print(" 1. Nowa gra")
    print(" 2. Ustawienia")
    print(" 3. Wyjście")
    answer = input("> ")
    match(ck(3, answer)):
        case 1: return 1
        case 2: return options()
        case 3: return 0

def options(): #zakładka ustawień w menu
    global hud
    global lang
    clear()
    intro()
    print(" 1. HUD: "+ hud)
    print(" 2. Language: "+ lang)
    print(" 3. Exit")
    match(ck(3, input("> "))):
        case 1:
            if hud == 'on':
                hud = 'off'
            else:
                hud = 'on'
            return options()
        case 2:
            if lang == 'pl':
                lang = 'en'
            elif lang == 'en':
                lang = 'de'
            else:
                lang = 'pl'
            return options()
        case 3: return menu()

def ck(opt, ans): #funkcja sprawdza czy to co wprowadzi użytkownik może być traktowane jako decyzję, oraz czy użytkownik w ogóle wprowadził cyfrę
    #if(ans == '0'):
    #    menu()
    # przygotowana funkcja w razie gdyby w przyszłości użytkownik miał miec opcję przerwania i zapisania gry
    while(ans.isdigit() == False):
        ans = input("Proszę wprowadzić prawidłową cyfrę \n> ")
    ans = int(ans)
    while(opt < ans or ans < 0):
        ans = input("Nie ma takiej opcji \n> ")
        while(ans.isdigit() == False):
            ans = input("Proszę wprowadzić prawidłową cyfrę \n> ")
        ans = int(ans)
    return ans

def rf(line): #system wyciągania linijki tekstu z pliku dialogues.txt, przekazuje również który język czytać na podstawie zmiennej lang
    global lang
    if (lang == 'pl'):
        file = 'polish.txt'
    elif (lang == 'en'):
        file = 'english.txt'
    else:
        file = 'german.txt'
    with open(os.getcwd()+"\\"+file, 'r', encoding="UTF-8") as f:
        zmienna = f.readlines()
        return zmienna[line]
def newgame(): #odgrywa prolog
    global hp, dmg, cash, kev
    hp = 100
    dmg = 10
    cash = 50
    kev = 0
    end = 0
    while(end == 0):
        for i in range(23):
            hub()
            print(rf(i))
            input("Naciśnij enter aby kontynuować")
        hub()
        print(rf(23))
        print(rf(24))
        match(ck(2, input("> "))):
            case 1:
                hub()
                print(rf(25))
            case 2:
                hub()
                print(rf(25))
        input("Naciśnij enter aby kontynuować")
        end = 1
