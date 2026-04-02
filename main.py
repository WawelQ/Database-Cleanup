import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

# Przygotowanie połączenia z bazą danych
connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

# Próba połączenia z bazą danych
try:
    with connection.cursor() as cursor:
        # Przygotowanie zapytania SQL do bazy danych
        sql = "DELETE FROM bookings WHERE date < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)"
        wynik = cursor.execute(sql) # Wykonanie zapytania        
        connection.commit() # Zatwierdzenie zmian w bazie danych
        print(f"Ilosc usunietych rekordow: {wynik}") # Wyświetlenie ile rekordów zostało usuniętych
except pymysql.Error as e:
    connection.rollback() # Cofnięcie zmian jeśli wystąpił błąd
    print(f"Wystapil blad: {e}")
    raise
finally:
    connection.close() # Zamknięcie połączenia z bazą danych po zakończeniu operacji