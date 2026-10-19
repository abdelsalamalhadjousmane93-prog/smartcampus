class LoginService  :
""" Service simulant la validation des identifiants (ticket SC-11)."""
MIN_PASSWORD_LENGTH =8
def validate(self , username , password):
if not username or not username.strip():
return False
if not password or len(password) <self.MIN_PASSWORD_LENGTH:
return False
return True
