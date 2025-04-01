import pymssql
import pytest
import csv
import decimal

DB_CONFIG = {
    "server": "EPUAKYIW061B",  
    "database": "AdventureWorks2012",
    "username": "NewUserLogin",  
    "password": "StrongPassword123"
}

def get_db_connection():
    return pymssql.connect(
        server=DB_CONFIG["server"],
        user=DB_CONFIG["username"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )


@pytest.fixture(scope="module")
def db_connection():
    conn = get_db_connection()
    yield conn
    conn.close()


@pytest.fixture(scope="session", autouse=True)
def reset_report():
    with open("test_report.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Query", "Actual Result", "Expected Result", "Test Status"])


@pytest.mark.parametrize("query, expected", [
    ("SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address] WHERE YEAR(ModifiedDate) = 2009", 135),
    ("SELECT MAX(ModifiedDate) FROM [AdventureWorks2012].[Person].[Address]", "2014-06-30 00:00:00"),
    (
    "SELECT TOP 1 FileName FROM [AdventureWorks2012].[Production].[Document] ORDER BY ROW_NUMBER() OVER (PARTITION BY Owner ORDER BY Filename ASC)",
    "Assembly"),
    (
    "SELECT CAST(AVG(CAST(DocumentLevel AS DECIMAL(10,2))) AS DECIMAL(10,2)) FROM [AdventureWorks2012].[Production].[Document]",
    1.62),
    ("SELECT MIN(Name) FROM [AdventureWorks2012].[Production].[UnitMeasure]", "Bottle"),
    ("SELECT COUNT(UnitMeasureCode) FROM [AdventureWorks2012].[Production].[UnitMeasure]", 38)
])
def test_sql_query(db_connection, query, expected):
    cursor = db_connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()[0]

    if isinstance(result, decimal.Decimal):  
        result = float(result)
    if isinstance(expected, str):  
        result = str(result)

    test_status = "Passed" if result == expected else "Failed"

    with open("test_report.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([query, result, expected, test_status])

    assert result == expected, f"Expected {expected}, but got {result}"
