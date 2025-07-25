# generate_seeds.py
import pandas as pd
from faker import Faker
import random
from pathlib import Path

fake = Faker('pt_BR')
seeds_path = Path("seeds")
seeds_path.mkdir(exist_ok=True)

# Configurações
NUM_CUSTOMERS = 50
NUM_PRODUCTS = 20
NUM_ORDERS = 100
NUM_ORDER_ITEMS = 250
NUM_PAYMENTS = 100

# Clientes
customers = [
    {
        "customer_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "created_at": fake.date_between(start_date='-2y', end_date='today')
    }
    for i in range(1, NUM_CUSTOMERS + 1)
]
pd.DataFrame(customers).to_csv(seeds_path / "raw_customers.csv", index=False)

# Produtos
products = [
    {
        "product_id": i,
        "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "category": random.choice(["Eletrônicos", "Vestuário", "Casa", "Esportes"]),
        "price": round(random.uniform(10.0, 1000.0), 2)
    }
    for i in range(1, NUM_PRODUCTS + 1)
]
pd.DataFrame(products).to_csv(seeds_path / "raw_products.csv", index=False)

# Pedidos
orders = [
    {
        "order_id": i,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "order_date": fake.date_between(start_date='-1y', end_date='today'),
        "status": random.choice(["completed", "processing", "canceled"])
    }
    for i in range(1, NUM_ORDERS + 1)
]
pd.DataFrame(orders).to_csv(seeds_path / "raw_orders.csv", index=False)

# Itens do pedido
order_items = [
    {
        "order_item_id": i,
        "order_id": random.randint(1, NUM_ORDERS),
        "product_id": random.randint(1, NUM_PRODUCTS),
        "quantity": random.randint(1, 5),
        "unit_price": round(random.uniform(10.0, 1000.0), 2)
    }
    for i in range(1, NUM_ORDER_ITEMS + 1)
]
pd.DataFrame(order_items).to_csv(seeds_path / "raw_order_items.csv", index=False)

# Pagamentos
payments = [
    {
        "payment_id": i,
        "order_id": i,  # simplificação: 1 pagamento por pedido
        "payment_method": random.choice(["credit_card", "boleto", "pix"]),
        "amount": round(random.uniform(50.0, 2000.0), 2),
        "payment_date": fake.date_between(start_date='-1y', end_date='today')
    }
    for i in range(1, NUM_PAYMENTS + 1)
]
pd.DataFrame(payments).to_csv(seeds_path / "raw_payments.csv", index=False)

print("✅ Dados seeds gerados com sucesso!")
