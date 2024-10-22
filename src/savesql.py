import pyodbc
import main as ma

connection_data = (
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=DESKTOP-EO6D9UQ\OLAP1;"
    r"DATABASE=Ecommerce;"
    r"UID=sa;"
    r"PWD=123456"
)

connection = pyodbc.connect(connection_data)
cursor = connection.cursor()

def main():

    df = ma.processing_data()
    
    for index, row in df.iterrows():
        cursor.execute('''
            INSERT INTO Sellings (sale_date, Customer, Brand, Model, Price, Payment_method, Country)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            row['sale_date'], 
            row['customer'], 
            row['brand'], 
            row['model'], 
            row['price'], 
            row['payment_method'], 
            row['Country'])
    
    connection.commit()
    cursor.close
    connection.close()

if __name__ == '__main__':
    main()


