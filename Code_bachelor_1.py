import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Monatliche Lithiumpreise 2021-2023
lithium_prices = [ 
    62500, 70500, 85000, 90000, 89000, 89000, 91000, 117000, 176000, 192500, 198500, 277500,
    377500, 483500, 496500, 462500, 468500, 475500, 476500, 492500, 510500, 565500, 577500, 519500,
    474500, 370500, 229500, 177500, 297500, 307500, 264500, 201500, 166500, 163500, 115000, 96500
]

# Monatliche Nickel-Metall-Preise 2021-2023
nickel_prices = [
   17863.2,18584.4,16406.7,16521.2 ,17602.1,17979.6,18818.6,19141.3,19376.9,
   19362.4,19932.9,20015.5,22355.4,24015.5,
   33924.2,33133.8,28228.9,25877.1,21481.9,22034.9,22774,22032.9,25562.7,
   28985.9,28271.5,26727.9,23288.6,23770.8,22134.8,21233.3, 
   21091.3,20446.4,19644.6,18264,17027.4,16443.5
]
# Monatliche Kobalt Preise 2021-2023
cobalt_prices = [
    37883.78, 47516.45, 52414.67, 49020.70, 44214.85, 44149.36, 51649.02, 51640.50, 51797.91, 54779.29, 60412.50, 69347.19,
    70527.05, 71573.60, 80457.43, 81790.38, 77721.36, 72057.73, 55713.24, 49308.83, 51515.41, 51509.24, 51504.59, 51497.77,
    48874.36, 36615.01, 33865.13, 34498.75, 33139.63, 29350.64, 32982.30, 32980.65, 32981.88, 32982.75, 33003.73, 30025.67,
]

# Monatliche LME-Preise für 2021-2023
lme_prices = [  
    3455.8, 3876.9, 3787.1, 4178.1, 4349.6, 4151.5, 4320.6, 4292.4, 4161.0, 4394.2, 4326.9, 4502.0,  # 2021
    4582.2, 4855.8, 5174.3, 4830.8, 4537.0, 3878.6, 3850.9, 3739.4, 3541.0, 3487.1, 3923.5, 3983.8,  # 2022
    4356.3, 4031.2, 4038.2, 3907.6, 3627.9, 3681.1, 3913.5, 3717.6, 3716.9, 3602.0, 3643.2, 3762.1   # 2023
]

# DataFrame mit Datumsangaben für Lithium
dates = pd.date_range(start='2021-01-01', periods=len(lithium_prices), freq='M')
data = pd.DataFrame({'Date': dates, 'Lithium Prices': lithium_prices, 'LME Prices': lme_prices})

# DataFrame mit Datumsangaben für Nickel
dates2 = pd.date_range(start='2021-01-01', periods=len(nickel_prices), freq='M')
data2 = pd.DataFrame({'Date': dates2, 'Nickel Prices': nickel_prices, 'LME Prices': lme_prices})

# DataFrame mit Datumsangaben für Kobalt
dates3 = pd.date_range(start='2021-01-01', periods=len(cobalt_prices), freq='M')
data3 = pd.DataFrame({'Date': dates, 'Cobalt Prices': cobalt_prices, 'LME Prices': lme_prices})

# Indexierung der Werte mit dem Basiswert von 2021 (erster Wert der jeweiligen Reihe) (Lithium)
data['Lithium Indexed'] = 100 * data['Lithium Prices'] / lithium_prices[0]
data['LME Indexed'] = 100 * data['LME Prices'] / lme_prices[0]

# Indexierung der Werte mit dem Basiswert von 2021 (erster Wert der LME-Reihe und erster Wert der Nickelreihe) (Nickel)
data2['Nickel-Metal Indexed'] = 100 * data2['Nickel Prices'] / nickel_prices[0]
data2['LME Indexed'] = 100 * data2['LME Prices'] / lme_prices[0]

# Indexierung der Werte mit dem Basiswert von 2021 (erster Wert der jeweiligen Reihe) (Kobalt)
data3['Kobalt Indexed'] = 100 * data3['Cobalt Prices'] / cobalt_prices[0]
data3['LME Indexed'] = 100 * data3['LME Prices'] / lme_prices[0]



# Plot für Lithium und LME-Index (2021-2023)
plt.figure(figsize=(10, 6))

plt.plot(data['Date'], data['Lithium Indexed'], label='Lithiumcarbonat (>99.5% Reinheit)', color='blue')
plt.plot(data['Date'], data['LME Indexed'], label='LME-Index', color='orange')

# Formatierung Lithium Plot

plt.title('Preisentwicklung von Lithiumcarbonat und LME-Index (2021-2023)')
plt.xlabel('Datum in Jahre')
plt.ylabel('Indexierter Wert: (Basis Januar 2021 = 100)')
plt.legend(loc='upper left')
plt.grid(True)

plt.xlim([pd.Timestamp('2021-01-01'), pd.Timestamp('2023-12-31')])
plt.xticks(data['Date'][::12], labels=['2021', '2022', '2023'])
plt.ylim(50,950)

# Diagramm anzeigen Lithium vs. LME-Index

plt.tight_layout()
plt.show()



# Plot für Nickel-Metal und LME-Index (2021-2023)
plt.figure(figsize=(10,6))

# Plot der indexierten Preise Nickel
plt.plot(data2['Date'], data2['Nickel-Metal Indexed'], 
         label='Nickel-Metal (99.8%) (Indexiert)', color='blue', linestyle='-',
         linewidth=2)
plt.plot(data2['Date'], data2['LME Indexed'], 
         label='LME-Index (Indexiert)', color='red', linestyle='-', 
         linewidth=2)

# Formatierung Nickel Plot

plt.title('Preisentwicklung von Nickel-Metall und LME-Index (2021-2023)')
plt.xlabel('Datum in Jahre')
plt.ylabel('Indexierter Wert: (Basis: Januar 2021 = 100)') 
plt.legend(loc='upper left')
plt.grid(True)

# Anpassen der x-Achse und der Ticks (Nickel)
plt.xticks(data2['Date'][::12], labels=['2021', '2022', '2023'])  

# Begrenzung der x-Achse auf den Zeitraum von Januar 2021 bis Dezember 2023
plt.xlim([pd.Timestamp('2021-01-01'), pd.Timestamp('2023-12-31')])

# Diagramm anzeigen Nickel vs LME
plt.tight_layout()
plt.show()



# Plot für Kobalt (Kathodenqualität) und LME-Index (2021-2023)
plt.figure(figsize=(10,6))

# Plot der indexierten Preise Kobalt
plt.plot(data3['Date'], data3['Kobalt Indexed'], 
         label='Kobalt Kathodenqualität', color='blue', linestyle='-',
         linewidth=2)
plt.plot(data3['Date'], data3['LME Indexed'], 
         label='LME-Index (Indexiert)', color='yellow', linestyle='-', 
         linewidth=2)

# Formatierung Kobalt Plot


plt.title('Preisentwicklung von Kobalt (Kathodenqualität) und LME-Index (2021-2023)')
plt.xlabel('Datum in Jahre')
plt.ylabel('Indexierter Wert: (Basis: Januar 2021 = 100)') 
plt.legend(loc='upper left')
plt.grid(True)

# Anpassen der x-Achse und der Ticks (Kobalt)
plt.xticks(data2['Date'][::12], labels=['2021', '2022', '2023'])  

# Diagramm anzeigen
plt.tight_layout()
plt.show()




# Normierte HHI Werte - Balkendiagramm


# Daten aus Tabelle 51 (Anhang E)

rohstoffe = ["Lithium", "Nickel", "Kobalt", "Natürlicher Graphit"]
kategorien = ["Förderkapazität", "Reserven", "Veredelungskapazität"]

hhi_werte = [
    [2974.57, 1989.5, 4189],        # Lithium
    [2609.96, 2354.04, 2795.05],    # Nickel
    [5323.13, 3353, 5928.58],       # Kobalt
    [5690.66, 1653, 7225]           # Natürlicher Graphit
]

# Farben für die Kategorien
farben = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # Blau, Orange, Grün

# Positionen für die Balken
x_pos = np.arange(len(rohstoffe))  # [0, 1, 2, 3]
bar_width = 0.25  # Breite der Balken

# Initialisiere das Diagramm
fig, ax = plt.subplots(figsize=(10, 6))

# Plotte die Balken für jede Kategorie
for i, kategorie in enumerate(kategorien):
    # Verschieben der Balken je nach Kategorie
    bar_positions = x_pos + i * bar_width
    hhi_values = [hhi_werte[j][i] for j in range(len(rohstoffe))]
    ax.bar(bar_positions, hhi_values, width=bar_width, color=farben[i], label=kategorie)

# Anpassung der Achsen und Beschriftung
ax.set_xlabel("Rohstoffe")
ax.set_ylabel("HHI-Wert (normiert)")
ax.set_title("Normierter Herfindahl-Hirschman Index (85% Marktabdeckung)")
ax.set_xticks(x_pos + bar_width)  # Position der Rohstoffnamen
ax.set_xticklabels(rohstoffe)
ax.legend(title="Kategorien")

# Ausgabe des Diagramms

plt.tight_layout()
plt.show()

# Normierung der Werte für jede Spalte (also für jedes HHI-Kriterium)
normierte_werte = [
    [hhi_werte[j][i] / max(hhi_werte[k][i] for k in range(len(rohstoffe))) for j in range(len(rohstoffe))]
    for i in range(len(kategorien))
]

# Ausgabe der normierten Werte
print("Normierte HHI Werte nach risikoreichstem Wert der Kategorie:")
for i, kategorie in enumerate(kategorien):
    print(f"{kategorie}: {normierte_werte[i]}")


# Benchmark-Index Varianz Berechnung

var = np.cov(data['Lithium Indexed'],data['LME Indexed'])[1, 1]
print("Die Varianz des Benchmark LME Index ist " + str(var))


# Kovarianz von Lithium und Benchmark-Index und Risiko-Beta Berechnung aus 
# Quotient von 
# Kovarianz Lithium mit Benchmark-Index und Varianz Benchmark-Index (LME)

covLi = np.cov(data['Lithium Indexed'], data['LME Indexed'])[0, 1]
betaLi = covLi/var
print("Die Kovarianz zwischen Lithium und dem LME Index ist " + str(covLi))
print("Das Risikobeta von Lithium zu dem LME Index ist " + str(betaLi))


# Kovarianz von Nickel und Benchmark-Index und Risiko-Beta Berechnung aus 
# Quotient von 
# Kovarianz Nickel mit Benchmark-Index und Varianz Benchmark-Index (LME)


covNi = np.cov(data2['Nickel-Metal Indexed'], data2['LME Indexed'])[0,1]
betaNi = covNi/var

print("Die Kovarianz zwischen Nickel und dem LME Index ist " + str(covNi))
print("Das Risikobeta von Nickel zu dem LME Index ist " + str(betaNi))



# Kovarianz von Kobalt und Benchmark-Index und Risiko-Beta Berechnung aus 
# Quotient von 
# Kovarianz Kobalt mit Benchmark-Index und Varianz Benchmark-Index (LME)


covCo = np.cov(data3['Kobalt Indexed'], data3['LME Indexed'])[0,1]
betaCo = covCo/var

print("Die Kovarianz zwischen Kobalt und dem LME Index ist " + str(covCo))
print("Das Risikobeta von Kobalt zu dem LME Index ist " + str(betaCo))



# DataFrame erstellen Lithium Preise für Volatilitätsberechnung

df_lithium = pd.DataFrame(lithium_prices)

# Berechnung der monatlichen Renditen (logarithmische Rendite)
df_lithium['Rendite'] = np.log(df_lithium / df_lithium.shift(1))

# Anzeigen der logarithmierten Renditen
print(df_lithium['Rendite'])


# Standardabweichung der logarithmierten Renditen
monats_volatilitaet_lithium = pd.Series(df_lithium['Rendite']).std()

# Anzeigen der logarithmierten Renditen
print(monats_volatilitaet_lithium)

# Berechnung Annualisierung der Standardabweichung 

annualisierte_volatilität_lithium = monats_volatilitaet_lithium * np.sqrt(12)

# Anzeige Annualisierte Volatilität

print("Die Preisvolatilität gemessen als annualisierte Standardabweichung der "
      "monatlichen logarithmischen Renditen für Lithium in "
      "Kathodenqualität beträgt " + str(annualisierte_volatilität_lithium))


# DataFrame erstellen Nickel Preise für Volatilitätsberechnung

df_nickel = pd.DataFrame(nickel_prices)

# Berechnung der monatlichen Renditen (logarithmische Rendite)
df_nickel['Rendite'] = np.log(df_nickel / df_nickel.shift(1))

# Anzeigen der logarithmierten Renditen
print(df_nickel['Rendite'])


# Standardabweichung der logarithmierten Renditen
monats_volatilitaet_nickel = pd.Series(df_nickel['Rendite']).std()

# Anzeigen der logarithmierten Renditen
print(monats_volatilitaet_nickel)

# Berechnung Annualisierung der Standardabweichung 

annualisierte_volatilität_nickel = monats_volatilitaet_nickel * np.sqrt(12)

# Anzeige Annualisierte Volatilität

print("Die Preisvolatilität gemessen als annualisierte Standardabweichung der "
      "monatlichen logarithmischen Renditen für Nickel in "
      "Kathodenqualität beträgt " + str(annualisierte_volatilität_nickel))



# DataFrame erstellen Kobalt Preise für Volatilitätsberechnung

df_cobalt = pd.DataFrame(cobalt_prices)

# Berechnung der monatlichen Renditen (logarithmische Rendite)
df_cobalt['Rendite'] = np.log(df_cobalt / df_cobalt.shift(1))

# Anzeigen der logarithmierten Renditen
print(df_cobalt['Rendite'])


# Standardabweichung der logarithmierten Renditen
monats_volatilitaet_cobalt = pd.Series(df_cobalt['Rendite']).std()

# Anzeigen der logarithmierten Renditen
print(monats_volatilitaet_cobalt)

# Berechnung Annualisierung der Standardabweichung 

annualisierte_volatilität_cobalt = monats_volatilitaet_cobalt * np.sqrt(12)

# Anzeige Annualisierte Volatilität

print("Die Preisvolatilität gemessen als annualisierte Standardabweichung der "
      "monatlichen logarithmischen Renditen für Kobalt in "
      "Kathodenqualität beträgt " + str(annualisierte_volatilität_cobalt))



# ADP-Indikator Balkendiagramm (alle vier kritischen Rohstoffe + Normierung)

# Rohstoffe und ihre Werte
rohstoffe = ['Lithium', 'Kobalt', 'Nickel', 'Natürlicher Graphit']
werte = [7.87e-4, 1.48e-3, 3.15e-3, 2.94e-7]  # Originalwerte

# Werte normieren  # Normierung im Verhältnis zum Maximum
normierte_werte = [wert / max(werte) for wert in werte]  

# Erstellen eines Balkendiagramms mit normierten Werten
fig, ax = plt.subplots(figsize=(10, 6))

# Balkendiagramm zeichnen
ax.bar(rohstoffe, normierte_werte, color='green')
ax.set_xlabel('Rohstoffe')
ax.set_ylabel('Normierter ADP-Wert, logarithmiert')


# Y-Achse auf logarithmische Skala setzen
ax.set_yscale('log')


# Ausgabe normierte Werte
print("Normierte ADP-Werte nach risikoreichstem Wert:")
print(normierte_werte)

# Layout anpassen
plt.tight_layout()
plt.show()


#ADP-Indikator Balkendiagramm (Lithium, Kobalt, Nickel + Normierung)

# Rohstoffe und ihre Werte
rohstoffe = ['Lithium', 'Kobalt', 'Nickel']
werte = [7.87e-4, 1.48e-3, 3.15e-3]  # Originalwerte

# Werte normieren  # Normierung im Verhältnis zum Maximum
normierte_werte = [wert / max(werte) for wert in werte] 

# Erstellen eines Balkendiagramms mit normierten Werten
fig, ax = plt.subplots(figsize=(10, 6))

# Balkendiagramm zeichnen
ax.bar(rohstoffe, normierte_werte, color='blue')
ax.set_xlabel('Rohstoffe')
ax.set_ylabel('Normierter ADP-Wert')


# Ausgabe normierte-Werte

print(normierte_werte)

# Layout anpassen
plt.tight_layout()
plt.show()



# Durchführbarkeit der Förderung

    # Datensätze
rohstoffe = {
    "Lithium": {
        "Länder": ["Australien", "Chile", "China"],
        "Marktanteile": [46.95, 23.84, 14.21],
        "PPI": [84.10, 55.66, 14.35],
    },
    "Nickel": {
        "Länder": ["Indonesien", "Philippinen", "Russland", "Neu-Kaledonien", "Kanada", "Australien", "China"],
        "Marktanteile": [48.53, 10.65, 6.83, 6.13, 5.02, 4.72, 3.11],
        "PPI": [32.16, 23.47, 36.92, 55, 81.92, 84.10, 14.35],
    },
    "Kobalt": {
        "Länder": ["Kongo", "Indonesien", "Russland", "Australien"],
        "Marktanteile": [72.59, 4.87, 4.67, 2.88],
        "PPI": [24.93, 32.16, 36.92, 84.10],
    },
    "natürlicher Graphit": {
        "Länder": ["China", "Mosambik"],
        "Marktanteile": [74.73, 10.30],
        "PPI": [14.35, 21.42],
    },
}

# Berechnung der gewichteten PPI-Scores
scores = {}
for rohstoff, daten in rohstoffe.items():
    gewichteter_score = sum(m * p / 100 for m, p in zip(daten["Marktanteile"], daten["PPI"]))
    scores[rohstoff] = gewichteter_score

# Ausgabe der Ergebnisse

print ("Durchführbarkeit der Förderung Score:")
for rohstoff, score in scores.items():
    print(f"{rohstoff}: {score:.2f}")

# Erstelle Balkendiagramme
for rohstoff, daten in rohstoffe.items():
    länder = daten["Länder"]
    marktanteile = daten["Marktanteile"]
    ppi = daten["PPI"]

    x = np.arange(len(länder))  # Positionen der Gruppen

    fig, ax = plt.subplots(figsize=(10, 6))

    # Balkenplot erstellen
    bar_width = 0.4
    ax.bar(x - bar_width / 2, marktanteile, bar_width, label="Marktanteil (%)", color="blue")
    ax.bar(x + bar_width / 2, ppi, bar_width, label="PPI-Score", color="orange")

    # Achsen und Titel
    ax.set_xlabel("Länder")
    ax.set_ylabel("Werte")
    ax.set_title(f"Marktanteile und PPI-Scores für Förderländer von {rohstoff}")
    ax.set_xticks(x)
    ax.set_xticklabels(länder, rotation=45)
    ax.legend()

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()


# Durchführbarkeit der Veredelung


# Ease of Doing Business (edo) Score der Veredelungsländer
länder = ["China", "Argentinien", "Australien", "Finnland", "Indonesien", "Japan"]
edo_scores = [77.9, 59, 81.2, 80.2, 69.6, 78]

# Erstelle Balkendiagramm
x = np.arange(len(länder))

fig, ax = plt.subplots(figsize=(12, 6))

# Balkenplot in Blau
ax.bar(x, edo_scores, color="red", label="Ease of Doing Business Score")

# Achsen und Titel
ax.set_xlabel("Länder")
ax.set_ylabel("Ease of Doing Business Score")
ax.set_title("Ease of Doing Business Scores der Veredelungsländer")
ax.set_xticks(x)
ax.set_xticklabels(länder, rotation=45)
ax.legend()

# Diagramm anzeigen
plt.tight_layout()
plt.show()   



# Daten für die Veredelungsländer
rohstoffe = {
    "Lithium": {
        "Länder": ["China", "Argentinien", "Australien"],
        "Marktanteile": [62.84, 12.5, 9.16],
        "EaseOfDoingBusiness": [77.9, 59, 81.2]
    },
    "Nickel": {
        "Länder": ["China", "Finnland", "Indonesien", "Japan"],
        "Marktanteile": [48, 16.98, 11.09, 8.93],
        "EaseOfDoingBusiness": [77.9, 80.2, 69.6, 78]
    },
    "Kobalt": {
        "Länder": ["China", "Finnland"],
        "Marktanteile": [76.53, 8.47],
        "EaseOfDoingBusiness": [77.9, 80.2]
    },
    "Natürlicher Graphit": {
        "Länder": ["China"],
        "Marktanteile": [85],
        "EaseOfDoingBusiness": [77.9]
    }
}

# Berechnung der gewichteten Ease-of-Doing-Business-Scores
scores = {}
for rohstoff, daten in rohstoffe.items():
    gewichteter_score = sum(m * e / 100 for m, e in zip(daten["Marktanteile"], daten["EaseOfDoingBusiness"]))
    scores[rohstoff] = gewichteter_score

# Ausgabe der Ergebnisse
print("Durchführbarkeit der Veredelung Score: ")
for rohstoff, score in scores.items():
    print(f"{rohstoff}: {score:.2f}")

# Erstelle Balkendiagramme
for rohstoff, daten in rohstoffe.items():
    länder = daten["Länder"]
    marktanteile = daten["Marktanteile"]
    ease_scores = daten["EaseOfDoingBusiness"]

    x = np.arange(len(länder))  # Positionen der Gruppen

    fig, ax = plt.subplots(figsize=(10, 6))

    # Balkenplot erstellen
    bar_width = 0.4
    ax.bar(x - bar_width / 2, marktanteile, bar_width, label="Marktanteil (%)", color="blue")
    ax.bar(x + bar_width / 2, ease_scores, bar_width, label="Ease of Doing Business Score", color="red")

    # Achsen und Titel
    ax.set_xlabel("Länder")
    ax.set_ylabel("Werte")
    ax.set_title(f"Marktanteile und Ease of Doing Business Scores für Veredelungsländer von {rohstoff}")
    ax.set_xticks(x)
    ax.set_xticklabels(länder, rotation=45)

    # Legende außerhalb des Diagramms platzieren, ohne das Diagramm zu verkleinern
    ax.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')

    # Sicherstellen, dass das Layout angepasst wird und das Diagramm nicht verkleinert wird
    plt.subplots_adjust(right=0.85)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()



# Geopolitische Risiken (World Governance Indikatoren)

# Daten: Länder und deren WGI-Werte
länder = [
    "Australien", "Chile", "China", "Indonesien", "Philippinen", 
    "Russland", "Neu-Kaledonien", "Kanada", "Kongo", "Mosambik", 
    "Argentinien", "Finnland", "Japan"
]
# Durchschnittliche aggregierte World-Governance-Indikator (wgi) Werte (Sechs Indikatoren)
wgi_werte = [
    92.705, 72.48, 41.97, 49.17, 42.61, 
    15.58, 40, 90.52, 7.26, 22.30, 
    42.73, 93.67, 89.75
]

# Mapping der Länder auf ihre WGI-Werte
wgi_mapping = dict(zip(länder, wgi_werte))

   # Datensätze Förderung, Marktanteile normiert
rohstoffe_förderung = {
    "Lithium": {
        "Länder": ["Australien", "Chile", "China"],
        "Marktanteile": [46.95, 23.84, 14.21],
    },
    "Nickel": {
        "Länder": ["Indonesien", "Philippinen", "Russland", "Neu-Kaledonien", "Kanada", "Australien", "China"],
        "Marktanteile": [48.53, 10.65, 6.83, 6.13, 5.02, 4.72, 3.11],
    },
    "Kobalt": {
        "Länder": ["Kongo", "Indonesien", "Russland", "Australien"],
        "Marktanteile": [72.59, 4.87, 4.67, 2.88],
    },
    "natürlicher Graphit": {
        "Länder": ["China", "Mosambik"],
        "Marktanteile": [74.73, 10.30],
    },
}

# Daten Veredelung, Marktanteile normiert
rohstoffe_veredelung = {
    "Lithium": {
        "Länder": ["China", "Argentinien", "Australien"],
        "Marktanteile": [62.84, 12.5, 9.16],
    },
    "Nickel": {
        "Länder": ["China", "Finnland", "Indonesien", "Japan"],
        "Marktanteile": [48, 16.98, 11.09, 8.93],
    },
    "Kobalt": {
        "Länder": ["China", "Finnland"],
        "Marktanteile": [76.53, 8.47],
    },
    "Natürlicher Graphit": {
        "Länder": ["China"],
        "Marktanteile": [85],
    }
}

# Funktion zur Berechnung des gewichteten WGI-Werts
def berechne_risiko(rohstoff_daten):
    risiko = {}
    for rohstoff, daten in rohstoff_daten.items():
        wert = sum(marktanteil * wgi_mapping[land] for land, marktanteil in zip(daten["Länder"], daten["Marktanteile"]))
        risiko[rohstoff] = wert / 100  # Normalisierung, da Marktanteile in Prozent gegeben sind
    return risiko

# Berechnung für Förderung und Veredelung
risiko_förderung = berechne_risiko(rohstoffe_förderung)
risiko_veredelung = berechne_risiko(rohstoffe_veredelung)

# Ausgabe der Ergebnisse
print("Geopolitische Stabilität Förderung:")
for rohstoff, risiko in risiko_förderung.items():
    print(f"{rohstoff}: {risiko:.2f}")  # Ausgabe mit zwei Nachkommastellen

print("\nGeopolitische Stabilität Veredelung:")
for rohstoff, risiko in risiko_veredelung.items():
    print(f"{rohstoff}: {risiko:.2f}")  # Ausgabe mit zwei Nachkommastellen
    
# Länder und Werte nach Ländernamen sortieren
sortierte_indices = np.argsort(länder)
länder_sortiert = np.array(länder)[sortierte_indices]
wgi_werte_sortiert = np.array(wgi_werte)[sortierte_indices]

# Plot erstellen
plt.figure(figsize=(12, 6))
plt.bar(länder_sortiert, wgi_werte_sortiert, color="skyblue")

# Titel und Achsenbeschriftungen
plt.title("World Governance Indicators (WGI) Werte pro Land", fontsize=14)
plt.xlabel("Länder (Index x)", fontsize=12)
plt.ylabel("WGI-Wert", fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()

# Plot anzeigen
plt.show()        


# Kapitel 6

# Risiko-Nachfrageerhöhungsmatrix 
# Gewichtungsmethode: Basis-Modell 
# Normierung: Relation zum risikoreichsten Wert

# Daten aus den Tabellen 14 und 31
rohstoffe = ['Lithium', 'Nickel', 'Kobalt', 'Natürlicher Graphit']
nachfrageerhöhung = [168.14, 245.95, 93.2, 197]  # Prozentuale Nachfrageerhöhung 2023-2030
gesamt_risikoscore = [59.74, 70.01, 80.42, 63.67]  # Gesamtrisikoscore (Förderung + Veredelung)

# Daten aus Kapitel 4.5.3 (CAGR-Werte) der kritischen Rohstoffe im Basis-Szenario
cagr_werte = [15.13, 19.4, 9.87, 16.84]

# Anfangswert
initial_value = 1

# Kategorisierung der x-Achsen-Bereiche: 
categories = ['5% CAGR', '10% CAGR', '15% CAGR', '20% CAGR', '25% CAGR']
category_bounds = [5, 10, 15, 20, 25]  # Grenzen in Prozent für die Kategorien

# Rohstoff-spezifische Farben
rohstoff_colors = ['blue', 'green', 'red', 'purple']

# Zuordnung der CAGR-Werte zu den Kategorien und proportionaler Berechnung der Position
x_positionen = []
for cagr in cagr_werte:
    for i in range(len(category_bounds) - 1):
        if category_bounds[i] <= cagr < category_bounds[i + 1]:
            # Berechnung der proportionalen Position innerhalb der Kategorie
            lower_bound = category_bounds[i]
            upper_bound = category_bounds[i + 1]
            proportional_position = (cagr - lower_bound) / (upper_bound - lower_bound)
            x_position = i + proportional_position
            x_positionen.append(x_position)
            break

# Erstellen des Plots
fig, ax = plt.subplots(figsize=(12, 6))  # Größere Breite für Klarheit
y_range = np.arange(0, 101, 10)

# Setzen der Achsenbeschriftungen und Gitter
ax.set_xticks(np.arange(len(categories)))  # Verwende die Länge der Kategorien für die Ticks
ax.set_xticklabels(categories)  # Beschrifte die Ticks mit den Kategorien
ax.set_yticks(y_range)
ax.set_yticklabels(map(str, y_range))
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xlim(-0.5, 4.5)  # Dehne die x-Achse nach rechts
ax.set_ylim(0, 100)

# Punkte plotten
for i, rohstoff in enumerate(rohstoffe):
    ax.scatter(x_positionen[i], gesamt_risikoscore[i], color=rohstoff_colors[i], label=f'{rohstoff} (CAGR:{cagr_werte[i]:.1f}%)', s=100)

# Titel und Achsenbeschriftungen
ax.set_title('Risiko-Nachfrageerhöhungsmatrix', fontsize=14, weight='bold')
ax.set_xlabel('Nachfrageerhöhung (CAGR 2023-2030)', fontsize=12)
ax.set_ylabel('Gesamtrisikoscore (Förderung + Veredelung)', fontsize=12)

# Legende
ax.legend(title='Kritische Rohstoffe', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Plot anzeigen
plt.tight_layout()
plt.show()



# Quadrantenanalyse der Risiko-Nachfrageerhöhungsmatrix
# Gewichtungsmethode: Basismodell
# Normierung: Relation zum risikoreichsten Wert

# Daten aus den Tabellen 14 und 31
rohstoffe = ['Lithium', 'Nickel', 'Kobalt', 'Natürlicher Graphit']
nachfrageerhöhung = [168.14, 245.95, 93.2, 197]  # Prozentuale Nachfrageerhöhung 2023-2030
gesamt_risikoscore = [59.74, 70.01, 80.42, 63.67]  # Gesamtrisikoscore (Förderung + Veredelung)

# Daten aus Kapitel 4.5.3 (CAGR-Werte) der kritischen Rohstoffe im Basis-Szenario
cagr_werte = [15.13, 19.4, 9.87, 16.84]

# Farben für die Rohstoffe
colors = {'Lithium': 'blue', 'Nickel': 'green', 'Kobalt': 'red', 'Natürlicher Graphit': 'purple'}

# Erstellen des Plots
fig, ax = plt.subplots(figsize=(12, 6))  # Größere Breite für Klarheit
y_range = np.arange(0, 101, 10)

# Setzen der Achsenbeschriftungen und Gitter
ax.set_xticks(np.arange(5))  # Verwende die Länge der Kategorien für die Ticks
ax.set_xticklabels(['5% CAGR', '10% CAGR', '15% CAGR', '20% CAGR', '25% CAGR'])
ax.set_yticks(y_range)
ax.set_yticklabels(map(str, y_range))
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xlim(-0.5, 4)  # Dehne die x-Achse bis zur vertikalen Linie bei 25% (x=4)
ax.set_ylim(0, 100)

# Punkte plotten
for i, rohstoff in enumerate(rohstoffe):
    ax.scatter(cagr_werte[i] / 5 - 1, gesamt_risikoscore[i], color=colors[rohstoff], label=f'{rohstoff} (CAGR:{cagr_werte[i]:.1f}%)', s=100)

# Linien für die Quadranten
ax.axvline(x=1.5, color='black', linestyle='--')  # Vertikale Linie bei 12.5% CAGR
ax.axhline(y=50, color='black', linestyle='--')  # Horizontale Linie bei Risiko=50

# Text in den Quadranten
ax.text(0.25, 90, 'Quadrant 1: \nHohes Risiko \nniedrige Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='blue')
ax.text(2.75, 90, 'Quadrant 2: \nHohes Risiko \nhohe Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='red')
ax.text(0.25, 10, 'Quadrant 3: \nNiedriges Risiko \nniedrige Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='orange')
ax.text(2.75, 10, 'Quadrant 4: \nNiedriges Risiko \nhohe Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='green')

# Titel und Achsenbeschriftungen
ax.set_title('Quadrantenanalyse', fontsize=14, weight='bold')
ax.set_xlabel('Nachfrageerhöhung (CAGR 2023-2030)', fontsize=12)
ax.set_ylabel('Gesamtrisikoscore (Förderung + Veredelung)', fontsize=12)

# Legende
ax.legend(title='Kritische Rohstoffe', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Plot anzeigen
plt.tight_layout()
plt.show()



# Quadrantenanalyse Risiko-Nachfrageerhöhungsmatrix 
# Gewichtungsmethode: Basismodell
# Normierung: Min-Max

# Daten aus den Tabellen 14 und 31
rohstoffe = ['Lithium', 'Nickel', 'Kobalt', 'Natürlicher Graphit']
nachfrageerhöhung = [168.14, 245.95, 93.2, 197]  # Prozentuale Nachfrageerhöhung 2023-2030
gesamt_risikoscore = [41.6, 36.93, 65.99, 52.61]  # Gesamtrisikoscore (Förderung + Veredelung)

# Daten aus Kapitel 4.5.3 (CAGR-Werte) der kritischen Rohstoffe im Basis-Szenario
cagr_werte = [15.13, 19.4, 9.87, 16.84]

# Feste Farbzuordnung für jedes Rohstoff
farben = {
    'Lithium': 'blue',
    'Nickel': 'green',
    'Kobalt': 'red',
    'Natürlicher Graphit': 'purple'
}

# Kategorisierung der x-Achsen-Bereiche:
categories = ['5% CAGR', '10% CAGR', '15% CAGR', '20% CAGR', '25% CAGR']
category_bounds = [5, 10, 15, 20, 25]  # Grenzen in Prozent für die Kategorien

# Zuordnung der CAGR-Werte zu den Kategorien und proportionaler Berechnung der Position
x_positionen = []
for cagr in cagr_werte:
    for i in range(len(category_bounds) - 1):
        if category_bounds[i] <= cagr < category_bounds[i + 1]:
            # Berechnung der proportionalen Position innerhalb der Kategorie
            lower_bound = category_bounds[i]
            upper_bound = category_bounds[i + 1]
            proportional_position = (cagr - lower_bound) / (upper_bound - lower_bound)
            x_position = i + proportional_position
            x_positionen.append(x_position)
            break

# Erstellen des Plots
fig, ax = plt.subplots(figsize=(12, 6))  # Größere Breite für Klarheit
y_range = np.arange(0, 101, 10)

# Setzen der Achsenbeschriftungen und Gitter
ax.set_xticks(np.arange(len(categories)))  # Verwende die Länge der Kategorien für die Ticks
ax.set_xticklabels(categories)  # Beschrifte die Ticks mit den Kategorien
ax.set_yticks(y_range)
ax.set_yticklabels(map(str, y_range))
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xlim(-0.5, 4)  # Dehne die x-Achse bis zur vertikalen Linie bei 25% (x=4)
ax.set_ylim(0, 100)

# Punkte plotten mit festen Farben
for i, rohstoff in enumerate(rohstoffe):
    ax.scatter(x_positionen[i], gesamt_risikoscore[i], color=farben[rohstoff], label=f'{rohstoff} (CAGR:{cagr_werte[i]:.1f}%)', s=100)

# Linien für die Quadranten
ax.axvline(x=1.5, color='black', linestyle='--')  # Vertikale Linie bei 12.5% CAGR
ax.axhline(y=50, color='black', linestyle='--')  # Horizontale Linie bei Risiko=50

# Text in den Quadranten
ax.text(0.25, 90, 'Quadrant 1: \nHohes Risiko \nniedrige Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='blue')
ax.text(2.75, 90, 'Quadrant 2: \nHohes Risiko \nhohe Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='red')
ax.text(0.25, 10, 'Quadrant 3: \nNiedriges Risiko \nniedrige Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='orange')
ax.text(2.75, 10, 'Quadrant 4: \nNiedriges Risiko \nhohe Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='green')

# Titel und Achsenbeschriftungen
ax.set_title('Quadrantenanalyse', fontsize=14, weight='bold')
ax.set_xlabel('Nachfrageerhöhung (CAGR 2023-2030)', fontsize=12)
ax.set_ylabel('Gesamtrisikoscore (Förderung + Veredelung) - Min-Max', fontsize=12)

# Legende
ax.legend(title='Kritische Rohstoffe', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Plot anzeigen
plt.tight_layout()
plt.show()



# Quadrantenanalyse Risikonachfrageerhöhungsmatrix
# Gewichtung: Basismodell vs. Indikatorengleichgewichtsmodell
# Normierung: Relation zum risikoreichsten Wert

# Daten aus der Tabelle 14 und 31
rohstoffe = ['Lithium', 'Nickel', 'Kobalt', 'Natürlicher Graphit']
nachfrageerhöhung = [168.14, 245.95, 93.2, 197]  # Prozentuale Nachfrageerhöhung 2023-2030
gesamt_risikoscore = [59.74, 70.01, 80.42, 63.67]  # Gesamtrisikoscore (Förderung + Veredelung)

# Daten aus Tabelle 33
gesamt_risiko_neugewichtung = [57.27, 68.27, 81.06, 63.68]  # Neugewichtet

# Daten aus Kapitel 4.5.3 (CAGR-Werte) der kritischen Rohstoffe im Basis-Szenario
cagr_werte = [15.13, 19.4, 9.87, 16.84]

# Farben für die Rohstoffe
farben = {
    'Lithium': 'blue',
    'Nickel': 'green',
    'Kobalt': 'red',
    'Natürlicher Graphit': 'purple'
}

# Kategorisierung der x-Achse-Bereiche: 
categories = ['5% CAGR', '10% CAGR', '15% CAGR', '20% CAGR', '25% CAGR']
category_bounds = [5, 10, 15, 20, 25]  # Grenzen in Prozent für die Kategorien

# Zuordnung der CAGR-Werte zu den Kategorien und proportionaler Berechnung der Position
x_positions = []
for cagr in cagr_werte:
    for i in range(len(category_bounds) - 1):
        if category_bounds[i] <= cagr < category_bounds[i + 1]:
            # Berechnung der proportionalen Position innerhalb der Kategorie
            lower_bound = category_bounds[i]
            upper_bound = category_bounds[i + 1]
            proportional_position = (cagr - lower_bound) / (upper_bound - lower_bound)
            x_position = i + proportional_position
            x_positions.append(x_position)
            break

# Erstellen des Plots
fig, ax = plt.subplots(figsize=(12, 6))  # Größere Breite für Klarheit
y_range = np.arange(0, 101, 10)

# Setzen der Achsenbeschriftungen und Gitter
ax.set_xticks(np.arange(len(categories)))  # Verwende die Länge der Kategorien für die Ticks
ax.set_xticklabels(categories)  # Beschrifte die Ticks mit den Kategorien
ax.set_yticks(y_range)
ax.set_yticklabels(map(str, y_range))
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xlim(-0.5, 4.5)  # Dehne die x-Achse nach rechts
ax.set_ylim(0, 100)

# Punkte plotten: Gesamtrisiko
for i, rohstoff in enumerate(rohstoffe):
    ax.scatter(x_positions[i], gesamt_risikoscore[i], color=farben[rohstoff], label=f'{rohstoff} (Basis)', s=100)

# Punkte plotten: Neugewichtetes Risiko
for i, rohstoff in enumerate(rohstoffe):
    ax.scatter(x_positions[i], gesamt_risiko_neugewichtung[i], color=farben[rohstoff], marker='x', label=f'{rohstoff} (Indikatoren-Gleichgewichtung)', s=100)

# Titel und Achsenbeschriftungen
ax.set_title('Risiko-Nachfrageerhöhungsmatrix', fontsize=14, weight='bold')
ax.set_xlabel('Nachfrageerhöhung (CAGR 2023-2030)', fontsize=12)
ax.set_ylabel('Gesamtrisiko (Förder- und Veredelungsperspektive)', fontsize=12)

# Legende hinzufügen
ax.legend(loc='best', fontsize=10)

# Plot anzeigen
plt.tight_layout()
plt.show()


# Quadrantenanalyse Risiko-Nachfrageerhöhungsmatrix
# Gewichtungsmethode: Basis vs. Indikatorengleichgewicht
# Normierung: Min-Max

# Daten aus den Tabellen 14 und 31
rohstoffe = ['Lithium', 'Nickel', 'Kobalt', 'Natürlicher Graphit']
nachfrageerhöhung = [168.14, 245.95, 93.2, 197]  # Prozentuale Nachfrageerhöhung 2023-2030
gesamt_risikoscore = [41.6, 36.93, 65.99, 52.61]  # Gesamtrisikoscore (Förderung + Veredelung)

# Daten aus Kapitel 4.5.3 (CAGR-Werte) der kritischen Rohstoffe im Basis-Szenario
cagr_werte = [15.13, 19.4, 9.87, 16.84]

# Kategorisierung der x-Achse-Bereiche:
categories = ['5% CAGR', '10% CAGR', '15% CAGR', '20% CAGR', '25% CAGR']
category_bounds = [5, 10, 15, 20, 25]  # Grenzen in Prozent für die Kategorien

# Farben für die Punkte basierend auf den Rohstoffen
colors = ['blue', 'green', 'darkblue', 'red']
point_colors = colors  # Weisen Sie die Farben direkt zu

# Zuordnung der CAGR-Werte zu den Kategorien und proportionaler Berechnung der Position
x_positionen = []
for cagr in cagr_werte:
    for i in range(len(category_bounds) - 1):
        if category_bounds[i] <= cagr < category_bounds[i + 1]:
            # Berechnung der proportionalen Position innerhalb der Kategorie
            lower_bound = category_bounds[i]
            upper_bound = category_bounds[i + 1]
            proportional_position = (cagr - lower_bound) / (upper_bound - lower_bound)
            x_position = i + proportional_position
            x_positionen.append(x_position)
            break

# Daten aus dem Indikator-Gleichgewichts-Modell (Anhang C)
indikator_gesamt_risikoscore = [35.5, 39.59, 68.1, 47.7]  # Indikator-Gleichgewichts-Modell 

# Erstellen des Plots
fig, ax = plt.subplots(figsize=(12, 6))  # Größere Breite für Klarheit
y_range = np.arange(0, 101, 10)

# Setzen der Achsenbeschriftungen und Gitter
ax.set_xticks(np.arange(len(categories)))  # Verwende die Länge der Kategorien für die Ticks
ax.set_xticklabels(categories)  # Beschrifte die Ticks mit den Kategorien
ax.set_yticks(y_range)
ax.set_yticklabels(map(str, y_range))
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xlim(-0.5, 4)  # Dehne die x-Achse bis zur vertikalen Linie bei 25% (x=4)
ax.set_ylim(0, 100)

# Punkte plotten
for i, rohstoff in enumerate(rohstoffe):
    ax.scatter(x_positionen[i], gesamt_risikoscore[i], color=point_colors[i], label=f'{rohstoff} (Basis-Modell)', s=100)

# Weitere Punkte als Kreuze für das Indikator-Gleichgewichts-Modell
for i, rohstoff in enumerate(rohstoffe):
    ax.scatter(x_positionen[i], indikator_gesamt_risikoscore[i], color=point_colors[i], marker='x', s=100, label=f'{rohstoff} (Indikator-Gleichgewichts-Modell)')

# Linien für die Quadranten
ax.axvline(x=1.5, color='black', linestyle='--')  # Vertikale Linie bei 12.5% CAGR
ax.axhline(y=50, color='black', linestyle='--')  # Horizontale Linie bei Risiko=50

# Text in den Quadranten
ax.text(0.25, 90, 'Quadrant 1: \nHohes Risiko \nniedrige Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='blue')
ax.text(2.75, 90, 'Quadrant 2: \nHohes Risiko \nhohe Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='red')
ax.text(0.25, 10, 'Quadrant 3: \nNiedriges Risiko \nniedrige Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='orange')
ax.text(2.75, 10, 'Quadrant 4: \nNiedriges Risiko \nhohe Nachfrage', ha='center', va='center', fontsize=10, weight='bold', color='green')

# Titel und Achsenbeschriftungen
ax.set_title('Quadrantenanalyse', fontsize=14, weight='bold')
ax.set_xlabel('Nachfrageerhöhung (CAGR 2023-2030)', fontsize=12)
ax.set_ylabel('Gesamtrisikoscore (Förderung + Veredelung) - Min-Max', fontsize=12)

# Legende
ax.legend(title='Kritische Rohstoffe', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Plot anzeigen
plt.tight_layout()
plt.show()

# Funktion zur Berechnung der Min-Max Normierung und Relation zum risikoreichsten Wert.
# Absolute Werte aus Kapitel 5 wurden für jeden Indikator in 'werte' eingefügt
# um die min-max normierten relativen Risikowerte zu erhalten.

def berechne_normierungen(werte):
    min_wert = min(werte)
    max_wert = max(werte)
    
    # Min-Max Normierung
    normierte_werte = [(wert - min_wert) / (max_wert - min_wert) * 100 for wert in werte]
    
    # Relation zum Maximalwert
    relation_max_werte = [(wert / max_wert) * 100 for wert in werte]
    
    # Ergebnisse ausgeben
    print("Originalwerte:", werte)
    print("Min-Max normierte Werte:", normierte_werte)
    print("Relationen zum Maximalwert:", relation_max_werte)
    return normierte_werte, relation_max_werte

# Beispielwerte
werte = [21.45,60.4,86.99,50.42]

# Berechnungen durchführen
berechne_normierungen(werte)
