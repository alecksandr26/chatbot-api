from .test_setup import *

class TestAnswerRegister(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)

    def test_register_answer_no_data(self):
        res = self.client.post(self.register_answer_url)
        self.assertEqual(res.status_code, 401)

    def test_register_answer_no_token(self):
        res = self.client.post(self.register_answer_url, self.pattern_data)
        self.assertEqual(res.status_code, 401)

    def test_register_answer(self):
        res = self.client.post(self.register_answer_url, self.answer_data,
                               **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 201)

class TestAnswerFetch(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)
        self.register_answer(self.answer_data)

    def test_get_answer(self):
        res = self.client.get(self.retrieve_answer_1_url,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 200)

    def test_get_answer_no_token(self):
        res = self.client.get(self.retrieve_answer_1_url)
        self.assertEqual(res.status_code, 401)

    def test_get_answer_bad_url(self):
        bad_retrieve_answer_url = reverse("retrieve_answer", args = str(2))
        res = self.client.get(bad_retrieve_answer_url,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 404)

    def test_get_multiple_answers(self):
        self.register_n_answers(self.n_answers)
        for i in range(1, self.n_answers + 1):
            res = self.client.get(reverse("retrieve_answer", kwargs = {"pk" : str(i + 1)}),
                                  **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
            self.assertEqual(res.status_code, 200)

class TestAnswerUpdate(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)
        self.register_answer(self.answer_data)

    def test_update_answer_data(self):
        new_answer_data = {"answer": "Hello", "intent": 1}
        res = self.client.put(self.update_answer_url, new_answer_data,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["answer"], "Hello")

    def test_update_answer_data_no_token(self):
        new_answer_data = {"answer": "Hello", "intent": 1}
        res = self.client.put(self.update_answer_url, new_answer_data)
        self.assertEqual(res.status_code, 401)



class TestAnswerDelete(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)
        self.register_answer(self.answer_data)

    def test_delete_answer(self):
        res = self.client.delete(self.delete_answer_1_url,
                                 **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 202)

    def test_delete_answer_no_token(self):
        res = self.client.delete(self.delete_answer_1_url)
        self.assertEqual(res.status_code, 401)        
