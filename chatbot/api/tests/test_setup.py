from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import *
import json
import copy


class TestSetUp(APITestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # urls
        self.register_user_url = reverse("register_user")
        
        self.register_intent_url = reverse("register_intent")
        self.list_intent_url = reverse("list_intent")
        self.retrieve_intent_1_url = reverse("retrieve_intent", args = str(1))
        self.update_intent_url = reverse("update_intent", kwargs = {"pk" : str(1)})
        
        self.register_pattern_url = reverse("register_pattern")
        self.list_pattern_url = reverse("list_pattern")
        self.retrieve_pattern_1_url = reverse("retrieve_pattern", kwargs = {"pk" : str(1)})
        self.update_pattern_url = reverse("update_pattern", kwargs = {"pk" : str(1)})
        
        self.register_answer_url = reverse("register_answer")
        self.list_answer_url = reverse("list_answer")
        self.retrieve_answer_1_url = reverse("retrieve_answer", kwargs = {"pk" : str(1)})
        self.update_answer_url = reverse("update_answer", kwargs = {"pk" : str(1)})
        
        self.get_token_url = reverse("get_token")
        self.refresh_token_url = reverse("refresh_token")

        # data
        self.user_data = {
            "username" : "pedrito",
            "password" : "pedrito"
        }


        self.admin_data = {
            "username" : "admin",
            "password" : "admin"
        }

        self.intent_data = {
            "tagname" : "Greetings"
        }
        
        self.pattern_data = {
            "pattern" : "Hey!!",
            "intent" : 1
        }

        self.answer_data = {
            "answer" : "Hello, my brother",
            "intent" : 1
        }

        self.n_intents = 100
        self.n_patterns = 100
        self.n_answers = 100

        # empty token
        self.token = ""

    def register_user(self):
        """register the user data"""
        res = self.client.post(reverse("register_user"), self.user_data)
        assert res.status_code == 201

    def register_admin(self):
        """Register an admin user"""
        u = User.objects.create_superuser(**self.admin_data)
        assert u.is_staff == True
        u.save()

    def get_token_admin(self):
        # Get the token
        res = self.client.post(self.get_token_url, self.admin_data)
        assert res.status_code == 200
        self.token = res.data["access"]


    def register_intent(self, intent_data):
        res = self.client.post(self.register_intent_url, intent_data,
                               **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        assert res.status_code == 201

    def register_pattern(self, pattern_data):
        res = self.client.post(self.register_pattern_url, pattern_data,
                               **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        assert res.status_code == 201
        
    def register_answer(self, answer_data):
        res = self.client.post(self.register_answer_url, answer_data,
                               **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        assert res.status_code == 201

    def register_n_intents(self, n):
        list_intents = []
        for i in range(0, n):
            intent_data = copy.copy(self.intent_data)
            intent_data["tagname"] += str(i)
            list_intents.append(intent_data)
        res = self.client.generic("POST", self.list_intent_url, json.dumps(list_intents),
                                  **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'},
                                  content_type = "application/json")
        assert res.status_code == 201

    def register_n_patterns(self, n):
        list_patterns = []
        for i in range(0, n):
            pattern_data = copy.copy(self.pattern_data)
            pattern_data["pattern"] += str(i)
            list_patterns.append(pattern_data)
        res = self.client.generic("POST", self.list_pattern_url, json.dumps(list_patterns),
                                  **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'},
                                  content_type = "application/json")
        assert res.status_code == 201

    def register_n_answers(self, n):
        list_answers = []
        for i in range(0, n):
            answer_data = copy.copy(self.answer_data)
            answer_data["answer"] += str(i)
            list_answers.append(answer_data)
        res = self.client.generic("POST", self.list_answer_url, json.dumps(list_answers),
                                  **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'},
                                  content_type = "application/json")
        assert res.status_code == 201
