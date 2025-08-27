import random

from src.core.pages.admin_page.logging_admin_panel import AdminPageLogging
from src.core.pages.admin_page.create_room_db_data import AdminPageCreateRooms

from config.logger.config_logger import get_logger



class TestAdminPageCreateRoom:

    def test_admin_page_create_room_db_data(self, driver, room_templates_list):
        """
        Creating a room via the admin panel using data from a database/file.
        Takes a random room template and checks that it appears in the interface.
        """

        # 1. Initialization and authorization
        login_admin_panel = AdminPageLogging(driver, 'https://automationintesting.online/admin')
        login_admin_panel.open()
        login_admin_panel.admin_page_loging()

        # 2. Creating a room
        create_room = AdminPageCreateRooms(driver)
        room = random.choice(room_templates_list)
        created_number_of_room = create_room.admin_page_create_room_db_data(room)

        # 3. Checking the creation of the room
        check_create_room = create_room.check_created_room(created_number_of_room).text


        assert created_number_of_room == check_create_room, (
            f"The number was expected {created_number_of_room}, but found {check_create_room}")

