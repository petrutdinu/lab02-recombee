import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException

# TODO 1: Configurare credentiale Recombee (la fel ca la Lab 02)
DB_NAME = 'dinu-dev'
PRIVATE_TOKEN = ''
REGION = 'eu-west'

# SDK-ul (v6) cere regiunea ca enum Region, nu ca text: 'eu-west' -> Region.EU_WEST
REGIUNI = {
    "eu-west": Region.EU_WEST,
}

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGIUNI[REGION.lower()])

# TODO 2: Incarcarea aceluiasi dataset folosit la Lab 02
PATH_DATASET = 'books.csv'

def valoare(x, tip):
    """Converteste o valoare din CSV la tipul cerut; valorile lipsa (NaN) devin None"""
    if pd.isna(x):
        return None
    return tip(x)

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)
    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []
    
    for index, row in df.iterrows():
        # TODO 3: Extrageti ID-ul unic al produsului din coloana corespunzatoare din CSV
        item_id = str(row['book_id'])
        
        # TODO 4: Mapati proprietatile definite anterior cu valorile din randul curent
        # Exemplu:
        properties = {
            "title": valoare(row['title'], str),
            "authors": valoare(row['authors'], str),
            "publication_year": valoare(row['publication_year'], int),
            "language": valoare(row['language'], str),
            "average_rating": valoare(row['average_rating'], float),
            "ratings_count": valoare(row['ratings_count'], int),
        }
        
        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creează automat item-ul dacă acesta nu există)
        requests.append(SetItemValues(item_id, properties, cascade_create=True))
        
        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print("S-a trimis un lot de 100 item-uri...")
            
    # Trimitem si restul ramanase (daca numarul total nu e multiplu de 100)
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()
