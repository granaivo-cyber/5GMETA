from keycloak import KeycloakAuthenticationError
from  py5gmeta.common import identity
import unittest

class Identity:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.client_id = ""
        self.client_secrert = ""
        self.url = ""
        self.realm = ""

class IdentityTestCase(unittest.TestCase):
    def setUp(self):
        self.genuine_username = ""
        self.genuine_user_password = ""
        self.rogue_user_name = "Alice"
        self.roque_user_password = ""
        self.realm_name = ""
        self.client_id = ""
        self.client_secret = ""
        self.identity_url = ""


    def test_genuine_user_authentication(self):
        auth_headers = identity.get_header_with_token(self.identity_url, self.realm_name, self.client_id,
                                                           self.client_secret, self.genuine_username, self.genuine_user_password)
        print(auth_headers)

    def test_rogue_user_authentication(self):
        self.assertRaises(KeycloakAuthenticationError, identity.get_header_with_token(self.identity_url, self.realm_name, self.client_id,
                                                           self.client_secret, self.rogue_user_name, self.roque_user_password) )