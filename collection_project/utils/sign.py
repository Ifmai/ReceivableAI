from django.core import signing
from collection_project.settings import SALT
from collection_project.settings import N8N_SALT

def encode_id(pk: int) -> str:
    return signing.dumps(pk, salt=SALT)

def decode_id(value: str) -> int:
    return signing.loads(value, salt=SALT)

def decode_key(value: str) -> str:
    return signing.loads(value, salt=N8N_SALT)