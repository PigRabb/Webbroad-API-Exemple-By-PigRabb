from django.test import TestCase

from .models import User

class AuthenticationTestCase(TestCase) :

    def setUp(self) :
        User.objects.create(email="sirimongkon.s@ku.th",password="123456789",username="PigRabb",
                            first_name="sirimongkon",last_name="semsa-nga",status=2)
        User.objects.create(email="BbarGip@gmail.com",password="987654321",username="BbarGip",
                            first_name="sirimongkon",last_name="semsa-nga",status=1)

        
        self.authorization_header_pigrabb = "Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk="

        self.authorization_header_bbargip = "Basic QmJhckdpcEBnbWFpbC5jb206OTg3NjU0MzIx"

    def test_decode_token_funtion(self) :
        self.assertEqual(decode_token(self.authorization_header_pigrabb),
                        {"email" : "sirimongkon.s@ku.th" , "password" : "123456789"})
        self.assertEqual(decode_token(self.authorization_header_user_status_0_or_1),
                        {"email" : "BbarGip@gmail.com" , "password" : "987654321"})

