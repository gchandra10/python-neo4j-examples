from neo4j import GraphDatabase
import yaml


def load_config():
    """Load configuration from the YAML file.

    Returns:
        dict: Configuration data.
    """
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


config = load_config()


def get_neo4j_connection():
    """Create a Neo4j connection using the configuration.

    Returns:
        Neo4J driver object.
    """
    return GraphDatabase.driver(
        config["neo4j"]["uri"],
        auth=(config["neo4j"]["user"], config["neo4j"]["password"]),
    )


def clear_database(driver):
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
