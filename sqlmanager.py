import sqlite3

def utworz_tabele():
    conn = sqlite3.connect('lokalne_dane.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wydarzenia (
            nazwa TEXT,
            data TEXT,
            miejsce TEXT,
            opis TEXT,
            link_zrodlowy TEXT
        )
    ''')
    conn.commit()
    conn.close()

def zapisz_lokalnie_sqlite(dane):
    conn = sqlite3.connect('lokalne_dane.db')
    cursor = conn.cursor()
    for event in dane:
        cursor.execute("INSERT INTO wydarzenia VALUES (?, ?, ?, ?, ?)",
                       (event['nazwa'], event['data'], event['miejsce'],
                        event.get('opis', ''), event.get('link_zrodlowy', '')))
    conn.commit()
    conn.close()
    print(f"Zapisano {len(dane)} wydarzeń do lokalnej bazy danych.")

# ... po zebraniu danych ...
zebrane_dane = scrape_strona_pierwsza(url)
if zebrane_dane:
    utworz_tabele()
    zapisz_lokalnie_sqlite(zebrane_dane)

# ... później, skrypt do wysyłania z SQLite do Appwrite ...
def wyslij_do_appwrite_z_sqlite():
    conn = sqlite3.connect('lokalne_dane.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nazwa, data, miejsce, opis, link_zrodlowy FROM wydarzenia")
    rows = cursor.fetchall()
    conn.close()

    client = Client()
    client.set_endpoint(APPWRITE_ENDPOINT)
    client.set_project(APPWRITE_PROJECT_ID)
    database = Database(client)

    for row in rows:
        wydarzenie = {
            'nazwa': row[0],
            'data': row[1],
            'miejsce': row[2],
            'opis': row[3],
            'link_zrodlowy': row[4]
        }
        try:
            result = database.create_document(
                database_id=APPWRITE_DATABASE_ID,
                collection_id=APPWRITE_COLLECTION_ID,
                data=wydarzenie
            )
            print(f"Wysłano do Appwrite: {result['$id']}")
        except Exception as e:
            print(f"Błąd wysyłania do Appwrite: {e}")

# wywołaj funkcję wyslij_do_appwrite_z_sqlite() kiedy chcesz przesłać dane