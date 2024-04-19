from .test_setup import *

class TestAnswerRegister(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)

    def test_register_answer_no_data(self):
        res = self.client.post(self.register_answer_url)
        self.assertEqual(res.status_code, 401)

    def test_register_pattern_no_token(self):
        res = self.client.post(self.register_answer_url, self.pattern_data)
        self.assertEqual(res.status_code, 401)

    def test_register_pattern(self):
        res = self.client.post(self.register_answer_url, self.answer_data,
                               **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 201)    
        

    


