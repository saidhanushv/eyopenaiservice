import pyodbc
from openai import AzureOpenAI


def truncate_content(content):
    if len(content) > 5497:
        return content[:5497] + '...'
    return content


# Azure OpenAI Credentials
client = AzureOpenAI(
    azure_endpoint="https://myopenaiservice007.openai.azure.com/",
    api_key="abc793f7ec894862920f65aedfa7ee02",
    api_version="2023-05-15"
)

# Azure SQL Database credentials
server = 'saidhanushserver.database.windows.net'
database = 'saidhanushdatabase007'
username = 'saidhanushserver'
password = 'Aizen101'

# Connection string
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
)

cursor = cnxn.cursor()

# Conversation with OpenAI Chat
messages = [
    {"role": "system", "content": "You are an expert in Machine Learning."},
    {"role": "user", "content": "What is linear regression?"},
    {"role": "assistant",
     "content": "Linear regression is a fundamental supervised learning algorithm in machine learning and statistics. "
                "It is used for predicting a continuous outcome variable (also called the dependent variable) based "
                "on one or more predictor variables (independent variables). The relationship between the predictor "
                "variables and the outcome is assumed to be linear."},
]

while True:
    user_input = input("You: ")

    # exit condition
    if user_input.lower() == 'exit':
        for message in messages:
            for role, content in message.items():
                content = truncate_content(content)
                insert_record_sql = """
                INSERT INTO QueryLogs(role, content)
                VALUES(?, ?)
                """
                cursor.execute(insert_record_sql, (role, content))
        print(messages)
        cnxn.commit()
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="saidhanushdeployement",
        messages=messages
    )

    assistant_msg = response.choices[0].message.content
    print("Assistant: ", assistant_msg)

    messages.append({"role": "assistant", "content": assistant_msg})

cursor.close()
cnxn.close()