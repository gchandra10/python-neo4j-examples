from neo4j import GraphDatabase
from db_config import *

driver = get_neo4j_connection()


def create_rows():
    with driver.session() as session:

        # session.run("CREATE (rachel:Customer {name: 'Rachel'}) ")
        # session.run("CREATE (card1:CreditCard {number: '1234567890123456'}) ")
        # session.run("CREATE (macys:Merchant {name: 'Macys'}) ")
        # session.run("CREATE (rachel)-[:OWNS]->(card1) ")
        # session.run("CREATE (tx1:Transaction {amount: 100, timestamp: datetime()}) ")
        # session.run("CREATE (card1)-[:USED_IN]->(tx1)-[:MADE_AT]->(macys)")

        query = (
            "CREATE (rachel:Customer {name: 'Rachel'}) "
            "CREATE (card1:CreditCard {number: '1234567890123456'}) "
            "CREATE (macys:Merchant {name: 'Macys'}) "
            "CREATE (rachel)-[:OWNS]->(card1) "
            "CREATE (tx1:Transaction {amount: 100, timestamp: datetime()}) "
            "CREATE (card1)-[:USED_IN]->(tx1)-[:MADE_AT]->(macys)"
        )

        # session.run(query)

        ## alternate way
        # session.execute_write(lambda tx: tx.run(query))


# This function is created inside db_config.py
clear_database(driver)

create_rows()

driver.close()
