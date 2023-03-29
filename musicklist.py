import pymongo

# Verbindung zur MongoDB-Instanz herstellen
client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

# Datenbank "Music" auswählen
db = client['Music']

# Kollektion "Interpret" erstellen und Daten einfügen
interpret = db['Interpret2']
interpret_data = {
    'name': 'Vahid',
    'genre': 'classic',
    'origin': 'Tehran'
}
interpret.insert_one(interpret_data)
# Kollektion "Musikstück" erstellen und Daten einfügen
musikstueck = db['Musikstück']
musikstuecke_data = [
    {
        'title': 'Immer Kopf hoch',
        'year': '2023',
        'album': 'DAS LOHNT ZU LEBEN',
        'interpret': interpret_data['_id']
    }
]
musikstueck.insert_many(musikstuecke_data)

# Verknüpfung der Kollektionen
musikstueck.create_index([('interpret', 2)])

print('Daten erfolgreich in MongoDB eingefügt.')