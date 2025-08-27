from src.core.pages.admin_page.logging_admin_panel import AdminPageLogging
from src.core.pages.admin_page.create_room import AdminPageCreateRoom


class TestAdminPageCreateRoom:

    def test_admin_page_create_room_hc(self, driver):
        """
        Creating a room via the admin panel (hardcode version).
        Used for local debugging without connecting to a database or files
        """

        # 1. Authorization in the admin panel
        login_admin_panel = AdminPageLogging(driver, 'https://automationintesting.online/admin')
        login_admin_panel.open()
        login_admin_panel.admin_page_loging()

        # 2. Creating a room
        create_room = AdminPageCreateRoom(driver)
        created_number_of_room = create_room.admin_page_create_room()

        # 3. Checking the creation of the room
        check_create_room = create_room.check_created_room(created_number_of_room).text

        assert created_number_of_room == int(check_create_room), (
            f"The number was expected {created_number_of_room}, but found {check_create_room}")

