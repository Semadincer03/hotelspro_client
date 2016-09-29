from hotelspro_client.book import BookProcessor

if __name__ == '__main__':
    params = {'checkin': '2016-09-30', 'checkout': '2016-10-03', 'pax': '1', 'destination_code': '11260',
              'client_nationality': 'tr', 'currency': 'USD'}


    book_processor = BookProcessor(usename, password)
    print book_processor.search(params)
