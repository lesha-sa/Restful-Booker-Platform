from src.core.pages.admin_page.create_room import AdminPageCreateRoom


class TestAdminPageCreateRoom:
    def test_admin_page_create_room(self, driver):
        loging = AdminPageCreateRoom(driver, 'https://automationintesting.online/admin')
        loging.open()
        loging.admin_page_loging()
        loging.admin_page_create_room()
