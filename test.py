# -*- coding: utf-8 -*-

import random
from unittest import TestCase
from unittest import main
from hotelspro_client.book import BookProcessor


class Test(TestCase):
    def __init__(self, *args, **kwargs):
        self.book_processor = BookProcessor('http://localhost:8000/api/v2/',
                                            'semadincer', 'qwer321')
        self.params = {'pax': '1', 'checkin': '2016-10-10',
                       'checkout': '2016-10-11', 'currency': 'USD',
                       'hotel_code': '10370d', 'client_nationality': 'tr'}
        super(Test, self).__init__(*args, **kwargs)

    def test_search(self):
        search_resp = self.book_processor.search(self.params)
        self.assertTrue(search_resp['next_page_code'] is None)
        self.assertTrue(isinstance(search_resp['count'], int))
        self.assertGreaterEqual(search_resp['count'], 0)
        self.assertTrue(isinstance(search_resp['results'], list))
        code = pick_a_product_code(search_resp)
        self.assertTrue(code is not None)

    def test_availability(self):
        search_resp = self.book_processor.search(self.params)
        code = pick_a_product_code(search_resp)
        availability_resp = self.book_processor.availability(code)
        self.assertTrue(isinstance(availability_resp['policies'], list))

    def test_provision(self):
        search_resp = self.book_processor.search(self.params)
        code = pick_a_product_code(search_resp)
        provision_resp = self.book_processor.provision(code)
        self.assertIn('code', provision_resp)
        self.assertTrue(isinstance(provision_resp['policies'], list))

    def test_book(self):
        search_resp = self.book_processor.search(self.params)
        code = pick_a_product_code(search_resp)
        provision_resp = self.book_processor.provision(code)
        self.assertIn('code', provision_resp)
        self.assertTrue(isinstance(provision_resp['policies'], list))
        book_resp = self.book_processor.book(provision_resp['code'],
                                             {'name': '1,test,test,adult'})
        self.assertIn('code', book_resp)
        self.assertEqual('succeeded', book_resp['status'])

    def test_bookings(self):
        search_resp = self.book_processor.search(self.params)
        code = pick_a_product_code(search_resp)
        provision_resp = self.book_processor.provision(code)
        self.assertIn('code', provision_resp)
        self.assertTrue(isinstance(provision_resp['policies'], list))
        book_resp = self.book_processor.book(provision_resp['code'],
                                             {'name': '1,test,test,adult'})
        self.assertIn('code', book_resp)
        self.assertEqual('succeeded', book_resp['status'])

        bookings_resp = self.book_processor.bookings(book_resp['code'])
        self.assertIn('code', bookings_resp)
        self.assertTrue(isinstance(book_resp['hotel_payment_info'], list))

    def test_cancel(self):
        search_resp = self.book_processor.search(self.params)
        code = pick_a_product_code(search_resp)
        provision_resp = self.book_processor.provision(code)
        self.assertIn('code', provision_resp)
        self.assertTrue(isinstance(provision_resp['policies'], list))
        book_resp = self.book_processor.book(provision_resp['code'],
                                             {'name': '1,test,test,adult'})
        self.assertIn('code', book_resp)
        self.assertEqual('succeeded', book_resp['status'])

        cancel_response = self.book_processor.cancel(book_resp['code'])
        self.assertIsInstance(cancel_response, dict)
        self.assertIn('code', cancel_response)


def pick_a_product_code(search_response):
    results = search_response['results']
    if results:
        hotel_products = random.choice(results)['products']
        random_product = random.choice(hotel_products)
        return random_product['code']
    return None


if __name__ == '__main__':
    main()
