# Lassú a PyCharm: Jobb klikk a lakatra a jobb alsó sarokban: PowerSafe mode (realtime IO ellenőrzések kikapcsolása)

# CTRL + SHIFT + F10 : Aktuálisan megnyitott fájt indítja el

# Interpreter beállítása: File/Settings/Projects/Python interpreter/Fogaskerék/Add/VirtualEnv/Make available to all project

# Induláskor az interpeter betöltni az összes packageket (ezért lassú) --> ezért kell virtual environment

# Terminál (CMD): python -V: python verziót visszaadja

# virtuális környezet aktiválsása: projekt mappán belül: venv\Scripts\activate.bat
# virtuális környezet deativálsása: projekt mappán belül: venv\Scripts\deaktivate.bat

print("Hello World")

# Változókezelés - alap adattípusok
# string - karakterlánc (array)
# name: str - notáció - ha hozzá írod akkor messziről látszik bárkinek hogy milyen a típusa

# függvőny főlá viszed az egeret + CTRL --> HELP
name: str = input("What is your name? ")

# f formatted string, amikor változót akarunk elhelyezni a szövegben
print(f"Hello {name}")

# egész sor kikommentelése: CTRL + /
# -> str - visszatérési érték string
# ' vagy " használata? lehet mind a 2őt fájlon belül is. USA-ban ', EU-ban " az elterjedtebb

# library importálása
import datetime
print(f"{datetime.datetime.now()} - Hello {name}")  # Aktuális dátum és idő beszúra, pl logoknál

# naming convencion: állandó változónév legyen csupa nagybetű
# funkció
def hello_xy(name: str = "hthdhrehd") -> str:   # naming convencion: függvénynél, metódusnál.
    # name egy bemeneti argumentum, megadott  default értékkel
    # --> str: jelöljük hogy stringgel tér vissza
    print("#"*50)
    if name == "hthdhrehd":
        name = input("What is your name? ")
        if name == "asd":
            print("asd")
    else:
        print(f"{datetime.datetime.now()} - I know you")
    return f"{datetime.datetime.now()} - Halihó {name}!"   # visszatérési érték - statement


print(hello_xy())           # függvény felhívás alap argumetnum értékkel - visszatérési érték kiprintelése
print(hello_xy("gdfgfd"))   # függvény felhívás egyedi argumentum értékkel (mivel egy argumentum van így tudni fogja, hogy melyik)
print(hello_xy(name="fghdgfd")) # függvény felhívás egyedi paraméter értékkel (argumentum nevének megadásával)

truefalse: bool = True      # Bool változó érték nagybetűvel

if truefalse:               # If vmi = true egyszerűsítve
    print("True")

if not truefalse:           # If vmi = false egyszerűsítve
    print("False")

# Identálás = behúzás  tabbal = 4db space karakter
	 # jobb alsó sarokban beállíttható 4spaces/tabs
	 # láthatósága:File/Settings/Editor/General/Appearance/Show whitespaces


# Commit Gitlabra Ctrl + K vagy zöl pipa ikon
# .idea mappában az IDE settinsei vannak benne