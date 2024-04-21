from .test_setup import *

class TestPatternRegister(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)

    def test_register_pattern_no_data(self):
        res = self.client.post(self.register_pattern_url)
        self.assertEqual(res.status_code, 401)

    def test_register_pattern_no_token(self):
        res = self.client.post(self.register_pattern_url, self.pattern_data)
        self.assertEqual(res.status_code, 401)

    def test_register_pattern(self):
        res = self.client.post(self.register_pattern_url, self.pattern_data,
                               **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 201)

class TestPatternFetch(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)
        self.register_pattern(self.pattern_data)

    def test_get_pattern(self):
        res = self.client.get(self.retrieve_pattern_1_url,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 200)

    def test_get_pattern_no_token(self):
        res = self.client.get(self.retrieve_pattern_1_url)
        self.assertEqual(res.status_code, 401)

    def test_get_pattern_bad_url(self):
        bad_retrieve_pattern_url = reverse("retrieve_pattern", args = str(2))
        res = self.client.get(bad_retrieve_pattern_url,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 404)

    def test_get_multiple_pattern(self):
        self.register_n_patterns(self.n_patterns)
        for i in range(1, self.n_patterns + 1):
            res = self.client.get(reverse("retrieve_pattern", kwargs = {"pk" : str(i + 1)}),
                                  **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
            self.assertEqual(res.status_code, 200)
            
class TestPatternUpdate(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)
        self.register_pattern(self.pattern_data)

    def test_update_pattern_data(self):
        new_pattern_data = {"pattern" : "Hello", "intent" : 1}
        res = self.client.put(self.update_pattern_url, new_pattern_data,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["pattern"], "Hello")

    def test_update_pattern_data_no_token(self):
        new_pattern_data = {"pattern" : "Hello", "intent" : 1}
        res = self.client.put(self.update_pattern_url, new_pattern_data)
        self.assertEqual(res.status_code, 401)


class TestPatternDelete(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)
        self.register_pattern(self.pattern_data)

    def test_delete_pattern(self):
        res = self.client.delete(self.delete_pattern_1_url,
                                 **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 202)

    def test_delete_pattern_no_token(self):
        res = self.client.delete(self.delete_pattern_1_url)
        self.assertEqual(res.status_code, 401)        
