import bcrypt

def hash_password(password: str) -> str:
    """ Hashing the password and returning it"""
    return  bcrypt.hashpw(password, bcrypt.gensalt()) # salt round 12 by default


def verify_password(password:str, hashed_password: str) -> bool:
    """match the password with hashed password by unhashing it"""
    return bcrypt.checkpw(password, hashed_password)