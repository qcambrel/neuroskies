import os

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Token:
    def __init__(self, token: str) -> None:
        self.token: str = token

class TokenHandler:
    def __init__(self) -> None:
        pass

def handler(event: dict, context: dict) -> dict:
    return {"statusCode": 200, "body": "Token Lambda"}