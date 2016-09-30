from hotelspro_client.book import BookProcessor

if __name__ == '__main__':
    params = {'checkin': '2016-10-03', 'checkout': '2016-10-05', 'pax': '1', 'destination_code': '11260',
              'client_nationality': 'tr', 'currency': 'USD'}

    book_processor = BookProcessor(username, password)

    print book_processor.search(params)
    #print book_processor.provision("EOTUIUMRIAAAAAAAAAAAAAAAAAAAAAAAAAHAXbKLQLidSjyppnOHdesYUCAAAAAAAAAAAAAAAHACAAAAAFi4EEHAAB7T6YWOOApvBPIxgAAAAAAAAAAABA")
    #print book_processor.book("P9284MTPUZD6",{'name':'1,sema,dincer,adult'})
    #print book_processor.bookings("BTN6G7PHG43M")
    #print book_processor.cancel("BTN6G7PHG43M")

