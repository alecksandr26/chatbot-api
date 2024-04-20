from .test_setup import *

class TestIntentRegister(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()

    def test_register_intent_no_data(self):
        res = self.client.post(self.register_intent_url)
        self.assertEqual(res.status_code, 401)

    def test_register_intent_no_token(self):
        res = self.client.post(self.register_intent_url, self.intent_data)
        self.assertEqual(res.status_code, 401)

    def test_register_intent(self):
        res = self.client.post(self.register_intent_url, self.intent_data,
                               **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 201)

    def test_register_list_intent(self):
        list_intents = []
        for i in range(0, self.n_intents):
            intent_data = copy.copy(self.intent_data)
            intent_data["tagname"] += str(i)
            list_intents.append(intent_data)
        res = self.client.generic("POST", self.list_intent_url, json.dumps(list_intents),
                                  **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'},
                                  content_type = "application/json")
        self.assertEqual(res.status_code, 201)

class TestIntentFetch(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)

    def test_get_intent(self):
        res = self.client.get(self.retrieve_intent_1_url,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 200)

    def test_get_intent_no_token(self):
        res = self.client.get(self.retrieve_intent_1_url)
        self.assertEqual(res.status_code, 401)

    def test_get_intent_bad_url(self):
        bad_retrieve_intent_url = reverse("retrieve_intent", args = str(2))
        res = self.client.get(bad_retrieve_intent_url,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 404)
        
    def test_get_multiple_intest(self):
        self.register_n_intents(self.n_intents)

        for i in range(1, self.n_intents + 1):
            url = reverse("retrieve_intent", kwargs={'pk': '10'})
            res = self.client.get(reverse("retrieve_intent", args = (str(i), )),
                                  **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
            self.assertEqual(res.status_code, 200)

class TestIntentUpdate(TestSetUp):
    def setUp(self):
        self.register_admin()
        self.get_token_admin()
        self.register_intent(self.intent_data)

    def test_update_intent_data(self):
        new_intent_data = {"tagname" : "Farewells"}
        res = self.client.put(self.update_intent_url, new_intent_data,
                              **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["tagname"], "Farewells")
        
    def test_update_intent_data_no_token(self):
        new_intent_data = {"tagname" : "Farewells"}
        res = self.client.put(self.update_intent_url, new_intent_data)
        self.assertEqual(res.status_code, 401)
