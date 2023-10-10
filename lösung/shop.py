from flask import Flask, render_template

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
    # Übersichtsseite anzeigen
    return render_template('home.html', produkte=produkte)

@app.route('/details/<id>')
def details(id):
    # prüfen, ob das Produkt existiert, sonst Fehlermeldung
    if int(id) not in produkte:
        return "Produkt nicht gefunden", 404
    
    # Detailseite zum Produkt anzeigen
    return render_template('details.html', produkt=produkte[int(id)])

# Server starten
if __name__ == '__main__':
    app.run(debug=True, port=3000)