# -*- coding: utf-8 -*-

from unittest import TestCase, main
from hotelspro_client.book import BookProcessor


class TestClient(TestCase):

    def __init__(self, *args, **kwargs):
        self._book_processor = BookProcessor("semadincer", "qwer321")
        self._search_resp = self._book_processor.search({"pax": "1",
                                                "checkin": "2016-10-03",
                                                "checkout": "2016-10-05",
                                                "currency": "USD",
                                                "hotel_code": "10370d",
                                                "client_nationality": "tr"})

        self._prod_code = self._search_resp['results'][0]['products'][0][
            'code']
        super(TestClient, self).__init__(*args, **kwargs)

    def test_search(self):
        # self.assertEqual(200, self._search_resp.status_code)
        # resp = self._search_resp.json()
        self.assertGreaterEqual(self._search_resp['count'], 1)

        self.assertIn(self._prod_code, self._prod_code)

    def test_search_failed(self):
        pass
        # resp = self._book_processor.search({"pax": "1",
        #                            "checkin": "2016-09-30",
        #                            "currency": "USD",
        #                            "hotel_code": self._hotel_code,
        #                            "client_nationality": "tr"})
        # self.assertEqual(400, resp.status_code)

    def test_availability(self):
        resp = self._book_processor.availability(self._prod_code)
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(resp, dict)
        #self.assertIn('meal_type', resp)
        self.assertIn('price', resp)
        self.assertIn('cost', resp)
        #self.assertIsInstance(resp['rooms'], list)

    def test_provision(self):
        resp = self._book_processor.provision(self._prod_code)
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIn(self._prod_code, resp)

    def test_book_and_cancel(self):
        prov_code = self._book_processor.provision(self._prod_code)
        resp = self._book_processor.book(prov_code,
                                         {'name': '1,test,test,adult'})
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIn(resp, resp)
        self.assertEqual('succeeded', resp['status'])

        resp = self._book_processor.cancel(resp['code'])
        self.assertIsInstance(resp, dict)
        self.assertIn('code', resp)

    def test_bookings(self):
        resp = self._book_processor.bookings()
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(resp, list)

        resp = self._book_processor.bookings(self._book_code)
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(resp, dict)

if __name__ == '__main__':
    main()