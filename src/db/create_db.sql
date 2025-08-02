CREATE TABLE room_templates (
    room_id SERIAL PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    room_type VARCHAR(50) NOT NULL,
    accessible BOOLEAN NOT NULL DEFAULT TRUE,
    price DECIMAL(10,2) NOT NULL,
    additional_services TEXT
);
INSERT INTO room_templates (room_number, room_type, accessible, price, additional_services)
VALUES
('101', 'Single', TRUE, 120.00, 'Wi-Fi, TV'),
('102', 'Double', FALSE, 180.00, 'Wi-Fi, Breakfast'),
('103', 'Family', TRUE, 250.00, 'Wi-Fi, TV, Breakfast, Pool');
