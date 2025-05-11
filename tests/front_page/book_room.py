from src.core.pages.front_page.booking_room import BookRoom

class TestBookRoom:
    def test_book_room(self, driver):
        book_room_page = BookRoom(driver, 'https://automationintesting.online')
        book_room_page.open()
        book_room_page.book_room()
        booking_confirmed = book_room_page.book_room()
        assert 'Booking Confirmed' == booking_confirmed