import psycopg2

def write_to_postgres(data):
    connection = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        host='localhost',
        port="5432",
        password='postgres'
    )
    cursor = connection.cursor()
    
    insert_query = """INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(insert_query, (
        data['user_id'], data['device_type'], data['ip'],
        data['device_id'], data['locale'], data['app_version'], data['create_date']
    ))

    connection.commit()
    cursor.close()
    connection.close()
