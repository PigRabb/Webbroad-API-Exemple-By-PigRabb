from base64 import b64decode
from ..models import User

def decode_token(token) :
    token_split = token.split(" ")
    user = b64decode(token_split[1]).decode("utf-8").split(":")   
    
    return {"email" : user[0] , "password" : user[1]}


def authentication(token) :
    user = decode_token(token)
    data = User.objects.filter(email=user["email"],password=user["password"])
    return data[0]




