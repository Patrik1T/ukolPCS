import physics

vyska = 100
earth_time = physics.fall_time(vyska, physics.EARTH_GRAVITY)
moon_time = physics.fall_time(vyska, physics.MOON_GRAVITY)
hmotnost = 1000
rychlost = 0.9 * physics.SPEED_OF_LIGHT
relathmotnost = physics.relathmotnost(hmotnost, rychlost)
vzdalenost = 343
teplota = 20
cas = physics.cas_zvuku(vzdalenost, teplota, physics.SPEED_OF_SOUND)

print(f"Doba pádu {vyska} metrů na Zemi: {earth_time:.2f} sekundy")
print(f"Doba pádu {vyska} metrů na Měsíci: {moon_time:.2f} sekundy")
print(f"Relativistická hmotnost tělesa: {relathmotnost:.2f} kg")
print(f"Zvuk urazí {vzdalenost} metrů při teplotě {teplota} °C za {cas:.2f} sekundy.")