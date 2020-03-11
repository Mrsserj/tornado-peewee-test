import tornado
from tornado.testing import AsyncTestCase, AsyncHTTPClient


class TestCase(AsyncTestCase):
    @tornado.testing.gen_test
    def test_http_fetch(self):
        client = AsyncHTTPClient()
        response = yield client.fetch("http://127.0.0.1:5000")
        self.assertEqual(200, response.code)
