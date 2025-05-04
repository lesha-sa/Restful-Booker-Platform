from src.core.pages.admin_page.logging_admin_panel import AdminPageLogging
from src.core.pages.admin_page.create_room import AdminPageCreateRoom

class TestAdminPageCreateRoom:
    def test_admin_page_create_room(self, driver):
        loging = AdminPageLogging(driver, 'https://automationintesting.online/admin')
        loging.open()
        loging.admin_page_loging()
        create_room = AdminPageCreateRoom(driver)
        create_room.admin_page_create_room()
