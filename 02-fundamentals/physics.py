'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.625 #? měsíční gravitace
SPEED_OF_LIGHT = 300000 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def fall_time(vyska, gravity):
    """
    Vypočítá dobu pádu tělesa ze zvolené výšky na Zemi nebo Měsíc.
    parametr vyska: Výška pádu v metrech
    parametr gravity: Hodnota tíhového zrychlení (Země nebo Měsíc)
    return: Doba pádu v sekundách
    """
    cas = (2 * vyska / gravity) ** 0.5
    return cas

def relathmotnost(hmotnost, rychlost):
    """
    Vypočítá relativistickou hmotnost tělesa při zadané rychlosti vzhledem k rychlosti světla.
    :parametr mass: Klidová hmotnost tělesa v kg
    :parametr velocity: Rychlost tělesa v m/s
    :return: Relativistická hmotnost v kg
    """
    relathmotnost = hmotnost / (1 - rychlost**2 / SPEED_OF_LIGHT**2) ** 0.5
    return relathmotnost

def cas_zvuku(vzdalenost, teplota, speed_of_sound):
    """
    Vypočítá čas, za který zvuk urazí zadanou vzdálenost při zadané teplotě.
    :param vzdalenost: Vzdálenost v metrech
    :param teplota: Teplota vzduchu v °C
    :param speed_of_sound: Rychlost zvuku ve vzduchu při teplotě 20 °C v m/s
    :return: Čas v sekundách
    """
    rychlost_zvuku = speed_of_sound + 0.6 * teplota
    cas = vzdalenost / rychlost_zvuku
    return cas
