from django.core.signing import TimestampSigner, BadSignature, SignatureExpired

signer = TimestampSigner(salt="password-reset")

TOKEN_EXPIRY_SECONDS = 3600  # 1 hour

def generate_password_reset_token(user):
    return signer.sign(user.pk)

def verify_password_reset_token(token):
    try:
        unsigned = signer.unsign(token, max_age=TOKEN_EXPIRY_SECONDS)
        return int(unsigned)
    except (BadSignature, SignatureExpired):
        return None
