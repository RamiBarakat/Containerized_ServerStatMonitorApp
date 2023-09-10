import unittest
from flask import Flask, jsonify
import apis

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = apis.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Welcome!")

    def test_cpu_route(self):
        response = self.app.get('/cpu')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data, list))
        for item in data:
            self.assertTrue(isinstance(item, dict))

    def test_mem_route(self):
        response = self.app.get('/mem')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data, list))
        for item in data:
            self.assertTrue(isinstance(item, dict))


    def test_disk_route(self):
        response = self.app.get('/disk')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data, list))
        for item in data:
            self.assertTrue(isinstance(item, dict))


    def test_cpu_now_route(self):
        response = self.app.get('/cpu_now')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data,dict))


    def test_mem_now_route(self):
        response = self.app.get('/mem_now')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data, dict))

    def test_disk_now_route(self):
        response = self.app.get('/disk_now')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data,dict))


if __name__ == '__main__':
    unittest.main()
