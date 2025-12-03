from django.core import signing
from collection_project.settings import SALT

def encode_id(pk: int) -> str:
    return signing.dumps(pk, salt=SALT)

def decode_id(value: str) -> int:
    return signing.loads(value, salt=SALT)
