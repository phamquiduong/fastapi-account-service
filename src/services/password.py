from pwdlib import PasswordHash


class PasswordService:
    password_hash = PasswordHash.recommended()

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return PasswordService.password_hash.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return PasswordService.password_hash.hash(password)
