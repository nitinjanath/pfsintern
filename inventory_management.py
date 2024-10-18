import sqlite3
from tabulate import tabulate
from datetime import datetime

# Initialize database connection
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create tables if they don't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity_sold INTEGER,
        sale_date TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
''')

conn.commit()

# Function to add a new product
def add_product(name, price, quantity):
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    print("Product added successfully.")

# Function to update product quantity
def update_product(product_id, quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    print("Product quantity updated.")

# Function to delete a product
def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    print("Product deleted successfully.")

# Function to record a sale
def record_sale(product_id, quantity_sold):
    sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO sales (product_id, quantity_sold, sale_date) VALUES (?, ?, ?)', (product_id, quantity_sold, sale_date))
    cursor.execute('UPDATE products SET quantity = quantity - ? WHERE id = ?', (quantity_sold, product_id))
    conn.commit()
    print("Sale recorded successfully.")

# Function to generate a sales report
def generate_sales_report():
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    print(tabulate(sales, headers=['Sale ID', 'Product ID', 'Quantity Sold', 'Sale Date'], tablefmt='pretty'))

# Function to generate an inventory report
def generate_inventory_report():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    print(tabulate(products, headers=['Product ID', 'Name', 'Price', 'Quantity'], tablefmt='pretty'))

# Main menu for the CLI interface
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product Quantity")
        print("3. Delete Product")
        print("4. Record Sale")
        print("5. Generate Sales Report")
        print("6. Generate Inventory Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product ID / name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(name, price, quantity)
        elif choice == '2':
            product_id = int(input("Enter product ID to update: "))
            quantity = int(input("Enter new quantity: "))
            update_product(product_id, quantity)
        elif choice == '3':
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == '4':
            product_id = int(input("Enter product ID for the sale: "))
            quantity_sold = int(input("Enter quantity sold: "))
            record_sale(product_id, quantity_sold)
        elif choice == '5':
            generate_sales_report()
        elif choice == '6':
            generate_inventory_report()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    conn.close()
