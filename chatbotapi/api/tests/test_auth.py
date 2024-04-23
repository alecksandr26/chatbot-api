from .test_setup import *

class TestRegisterUser(TestSetUp):
    def test_register_user_no_data(self):
        res = self.client.post(self.register_user_url)
        self.assertEqual(res.status_code, 400)
        
    def test_register_user(self):
        res = self.client.post(self.register_user_url, self.user_data)
        self.assertEqual(res.status_code, 201)


class TestTokenUser(TestSetUp):
    def setUp(self):
        self.register_user()
        self.register_admin()

    def test_get_token_no_data(self):
        res = self.client.post(self.get_token_url)
        self.assertEqual(res.status_code, 400)
        
    def test_get_token_bad_credentials(self):
        bad_user_data = {
            "username" : "pedrito",
            "password" : "cola"
        }
        res = self.client.post(self.get_token_url, bad_user_data)
        self.assertEqual(res.status_code, 401)

    def test_get_token(self):
        res = self.client.post(self.get_token_url, self.user_data)
        self.assertEqual(res.status_code, 200)


    def test_refresh_token(self):
        res = self.client.post(self.get_token_url, self.user_data)
        assert res.status_code == 200
        assert "refresh" in res.data.keys()
        
        refresh_token = res.data["refresh"]
        res = self.client.post(self.refresh_token_url, {"refresh" : refresh_token})
        self.assertEqual(res.status_code, 200)
        
    def test_admin_get_token(self):
        res = self.client.post(self.get_token_url, self.admin_data)
        self.assertEqual(res.status_code, 200)


