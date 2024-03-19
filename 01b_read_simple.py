from neo4j import GraphDatabase
from db_config import *

driver = get_neo4j_connection()

# Use a session to run queries
with driver.session() as session:
    # 1. Find all customers
    result = session.run("MATCH (c:Customer) RETURN c.name")
    print("All customers:")
    for record in result:
        print(record["c.name"])
        
    print("*" * 100)

    # 2. Find all transactions made at Macys
    result = session.run(
        "MATCH (tx:Transaction)-[:MADE_AT]->(m:Merchant) "
        "WHERE m.name = 'Macys' "
        "RETURN tx.amount, tx.timestamp"
    )
    print("\nTransactions at Macys:")
    for record in result:
        print(f"Amount: {record['tx.amount']}, Timestamp: {record['tx.timestamp']}")

    print("*" * 100)
    
    # 3. Find all credit cards owned by Ross
    result = session.run(
        "MATCH (ross:Customer {name: 'Ross'})-[:OWNS]->(card:CreditCard) "
        "RETURN card.number"
    )
    print("\nRoss's credit cards:")
    for record in result:
        print(record["card.number"])

    print("*" * 100)

    # 4. Find the customer who made a specific transaction
    result = session.run(
        "MATCH (c:Customer)-[:OWNS]->(card:CreditCard)-[:USED_IN]->(tx:Transaction) "
        "WHERE tx.amount = 120 "
        "RETURN c.name"
    )
    print("\nCustomer who made the transaction:")
    for record in result:
        print(record["c.name"])

    print("*" * 100)

    # 5. Find the merchants where Monica made transactions
    result = session.run(
        "MATCH (monica:Customer {name: 'Monica'})-[:OWNS]->(card:CreditCard)-[:USED_IN]->(tx:Transaction)-[:MADE_AT]->(m:Merchant) "
        "RETURN DISTINCT m.name"
    )
    print("\nMerchants where Monica made transactions:")
    for record in result:
        print(record["m.name"])

    print("*" * 100)

    # 6. Find the total amount spent by Chandler at Macys
    result = session.run(
        "MATCH (chandler:Customer {name: 'Chandler'})-[:OWNS]->(card:CreditCard)-[:USED_IN]->(tx:Transaction)-[:MADE_AT]->(macys:Merchant {name: 'Macys'}) "
        "RETURN SUM(tx.amount) AS total_spent"
    )
    print("\nTotal amount spent by Chandler at Macys:")
    for record in result:
        print(record["total_spent"])

    print("*" * 100)


# Close the driver
driver.close()
