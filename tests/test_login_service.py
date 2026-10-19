import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from login_service import LoginService


class TestLoginService(unittest.TestCase):
    def setUp(self):
        self.service = LoginService()

    def test_identifiants_valides(self):
        self.assertTrue(self.service.validate("etudiant", "motdepasse123"))

    def test_identifiant_vide(self):
        self.assertFalse(self.service.validate("", "motdepasse123"))

    def test_mot_de_passe_trop_court(self):
        self.assertFalse(self.service.validate("etudiant", "court"))


if __name__ == "__main__":
    unittest.main()