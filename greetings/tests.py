"""Define tests for entire module"""
import json
from django.test import Client, TestCase, tag
from rest_framework import status
from .models import Greeting

TYPE = 'greeting'
PATH = '/greetings/'
CONTENT_TYPE = 'application/vnd.api+json'


class GreetingsTests(TestCase):
    """Test CRUD"""

    def setUp(self):
        self.client = Client()

    @tag('integration')
    def test_reading(self):
        """test reading"""
        response = self.client.get(PATH)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.client.get(PATH)

        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_creating(self):
        """test creating"""

        arbitrary_message = 'A Greeting'
        json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'message': arbitrary_message
                }
            }
        }

        response = self.client.post(
            PATH,
            json.dumps(json_data),
            content_type=CONTENT_TYPE,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_message = arbitrary_message
        self.assertEqual(
            Greeting.objects.first().message,
            expected_message
        )

    @tag('integration')
    def test_updating(self):
        """test updating"""

        original_message = 'Original Greeting'
        original_json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'message': original_message
                }
            }
        }
        response = self.client.post(
            PATH,
            json.dumps(original_json_data),
            content_type=CONTENT_TYPE
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_message = original_message
        self.assertEqual(
            Greeting.objects.first().message,
            expected_message
        )

        greeting_id = response.json()['data']['id']
        updated_message = 'Updated Greeting'
        updated_json_data = response.json()
        updated_json_data['data']['attributes']['message'] = updated_message
        response = self.client.patch(
            PATH + greeting_id + '/',
            data=json.dumps(updated_json_data),
            content_type=CONTENT_TYPE,
        )
        expected_message = updated_message
        self.assertEqual(
            Greeting.objects.get(pk=greeting_id).message,
            expected_message
        )

    @tag('integration')
    def test_deleting(self):
        """test deleting"""

        no_greetings = 0
        self.assertEqual(
            Greeting.objects.count(),
            no_greetings
        )

        json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'message': 'An Arbitrary Greeting'
                }
            }
        }

        response = self.client.post(
            PATH,
            json.dumps(json_data),
            content_type=CONTENT_TYPE,
        )
        greeting_id = response.json()['data']['id']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        one_new_greeting = 1
        self.assertEqual(
            Greeting.objects.count(),
            one_new_greeting
        )

        response = self.client.delete(
            PATH + greeting_id + '/',
            json.dumps(json_data),
            content_type=CONTENT_TYPE,
        )
        self.assertEqual(
            Greeting.objects.count(),
            no_greetings
        )

    @tag('integration')
    def test_full_lifecycle(self):
        """test full lifecycle"""

        original_message = 'A Greeting'
        json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'message': original_message
                }
            }
        }

        response = self.client.post(
            PATH,
            json.dumps(json_data),
            content_type=CONTENT_TYPE,
        )
        greeting_id = response.json()['data']['id']
        updated_json_data = response.json()

        expected_message = original_message
        self.assertEqual(
            Greeting.objects.get(pk=greeting_id).message,
            expected_message
        )

        response = self.client.get(PATH)
        first_greeter = 0
        self.assertEqual(
            (response.json()
                ['data'][first_greeter]
                ['attributes']['message']
             ),
            expected_message
        )

        updated_message = 'Updated Greeting'
        updated_json_data['data']['attributes']['message'] = updated_message
        response = self.client.patch(
            PATH + greeting_id + '/',
            data=json.dumps(updated_json_data),
            content_type=CONTENT_TYPE,
        )
        expected_message = updated_message
        self.assertEqual(
            Greeting.objects.get(pk=greeting_id).message,
            expected_message
        )

        response = self.client.delete(
            PATH + greeting_id + '/',
        )
        no_greetings = 0
        self.assertEqual(
            Greeting.objects.count(),
            no_greetings
        )

