import csv

def read_websites_from_csv(filepath='data/list.csv'):
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)  # Use csv.reader instead of DictReader
        return [f"https://{row[0]}" for row in reader]


def store_data(data, connection):
    cursor = connection.cursor()
    query = """
    INSERT INTO website_data (url, contact_email, contact_address, contact_number, language, cms_mvc, category)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)
    connection.commit()

def export_to_csv(data, filepath='data/website_data.csv'):
    import csv
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Contact Email', 'Contact Address', 'Contact Number', 'Language', 'CMS/MVC', 'Category'])
        for row in data:
            writer.writerow(row)
