from src.core.pages.admin_page.logging_admin_panel import AdminPageLogging
from src.core.pages.admin_page.create_room import AdminPageCreateRoom

from config.logger.config_logger import get_logger

logger = get_logger()


class TestAdminPageCreateRoom:

    def test_admin_page_create_room(self, driver):
        """Test creating a room through the admin panel"""
        # 1. Initialization and authorization
        logger.info("The beginning of the test: creating a room through the admin panel")
        loging_admin_panel = AdminPageLogging(driver, 'https://automationintesting.online/admin')
        loging_admin_panel.open()
        loging_admin_panel.admin_page_loging()

        # 2. Creating a room
        create_room = AdminPageCreateRoom(driver)
        created_number_of_room = create_room.admin_page_create_room()
        logger.info(f"A room has been created with a number: {created_number_of_room}")

        # 3. Checking the creation of the room
        check_create_room = create_room.check_created_room(created_number_of_room).text
        logger.info(f"Found number in the interface: {check_create_room}")

        assert created_number_of_room == int(check_create_room), (f"I was expecting a number {created_number_of_room},"
                                                                  f" but found {check_create_room}")

        logger.success(f"Test passed. The room {created_number_of_room} successfully created and found")
