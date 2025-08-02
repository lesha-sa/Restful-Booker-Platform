from src.repository.room_template_repository import get_all_room_templates


def test_all_data():

    data = get_all_room_templates()
    first = data[1]
    print(data[0].price)
    print(first.price)
