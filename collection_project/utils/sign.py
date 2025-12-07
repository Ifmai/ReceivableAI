from django.core import signing
from collection_project.settings import SALT
from collection_project.settings import N8N

def encode_id(pk: int) -> str:
    return signing.dumps(pk, salt=SALT)

def decode_id(value: str) -> int:
    return signing.loads(value, salt=SALT)


def encode_key(pk: int) -> str:
    return signing.dumps(pk, salt=N8N)

def decode_key(value: str) -> int:
    return signing.loads(value, salt=N8N)