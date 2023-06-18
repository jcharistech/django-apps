from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select the endpoint
transport = AIOHTTPTransport(url="http://127.0.0.1:8000/graphql")

# Create Graphql client
client = Client(transport=transport,fetch_schema_from_transport=True)

# Make Query
query = gql(
    """
    query {
    blogpostsByLimit(limit:4){
        title
        message
    }
        
    }

    """
)

# Execute
result = client.execute(query)
print(result)