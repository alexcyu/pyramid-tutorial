import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        # Do the import inside the testing function to isolate things that may break the test
        from tutorial import hello_world

        # Create a dummy request for the test
        request = testing.DummyRequest()

        # Test the hello_world function with the dummy request and see what the response is
        response = hello_world(request)

        # You want the response to be code 200.  
        # Use the assertEqual function to check if the status_code of the response is 200
        # When 200 is changed to 404 the  test will fail because the status_code returned will be 200 and not 404
        self.assertEqual(response.status_code, 404)