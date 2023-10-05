# Flask imports
from flask import Flask, render_template

# unser App-Objekt
app = Flask(__name__)

produkte = {
    1: {
        'name': 'Apfel',
        'preis': 1.99,
        'bild': 'https://upload.wikimedia.org/wikipedia/commons/a/a6/Pink_lady_and_cross_section.jpg'
    },
    2: {
        'name': 'Birne',
        'preis': 2.99,
        'bild': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Pears.jpg'
    },
    3: {
        'name': 'Kiwis',
        'preis': 3.99,
        'bild': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Apteryx_mantelli_-Rotorua%2C_North_Island%2C_New_Zealand-8a.jpg/2560px-Apteryx_mantelli_-Rotorua%2C_North_Island%2C_New_Zealand-8a.jpg'
    }
}

@app.route('/')
def home():
    # TODO: produkte auf der Homepage anzeigen, mit Link auf die Detailseite
    
    pass # kann gelöscht werden, wenn die Funktion fertig ist

@app.route('... TODO hier eine geeignete Route eintragen ...')
def details(id):
    # TODO: Produkt mit der ID aus der URL auslesen und anzeigen (Template details.html)
    
    # TODO: falls eine ungültige id übergeben wird:
    # return "Produkt nicht gefunden", 404

    pass # kann gelöscht werden, wenn die Funktion fertig ist

# Server auf Port 3000 starten
if __name__ == '__main__':
    app.run(debug=True, port=3000)