from db import create_connection
from extractor import extract_info
from utils import store_data, export_to_csv, read_websites_from_csv

def main():
    connection = create_connection()
    if not connection:
        return
    
    websites = read_websites_from_csv()
    data_list = []

    for url in websites:
        data = extract_info(url)
        if data:
            store_data(data, connection)
            data_list.append(data)
    
    export_to_csv(data_list)
    connection.close()

if __name__ == "__main__":
    main()
