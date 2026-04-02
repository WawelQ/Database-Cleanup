import os
import pymysql
from dotenv import load_dotenv

load_dotenv() # Załadowanie pliku .env z konfiguracją programu

# Sprawdzenie czy wszystkie wymagane zmienne są ustawione w pliku .env
required = ['DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'DB_TABLE', 'DB_DATE_COLUMN', 'DB_INTERVAL']
missing = [var for var in required if not os.getenv(var)]
if missing:
    print(f"Brakuje wymaganych zmiennych w pliku .env: {', '.join(missing)}")
    raise

table = os.getenv('DB_TABLE') # Pobranie nazwy tabli z której będą usuwane dane
date = os.getenv('DB_DATE_COLUMN') # Pobranie nazwy kolumny w której przechowywana jest data
interval = os.getenv('DB_INTERVAL') # Pobranie czasu po którym rekordy mają być usunięte

# Przygotowanie połączenia z bazą danych
connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

# Próba połączenia z bazą danych
try:
    with connection.cursor() as cursor:
        # Przygotowanie zapytania SQL do bazy danych
        sql = f"DELETE FROM {table} WHERE {date} < DATE_SUB(CURDATE(), INTERVAL {interval})"
        deleted = cursor.execute(sql) # Wykonanie zapytania
        connection.commit() # Zatwierdzenie zmian w bazie danych
        print(f"Ilosc usunietych rekordow: {deleted} Starszych niz: {interval}") # Wyświetlenie ile rekordów zostało usuniętych
except pymysql.Error as e:
    connection.rollback() # Cofnięcie zmian jeśli wystąpił błąd
    print(f"Wystapil blad: {e}")
    raise
finally:
    connection.close() # Zamknięcie połączenia z bazą danych po zakończeniu operacji