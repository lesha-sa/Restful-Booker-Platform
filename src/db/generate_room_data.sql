CREATE TABLE room_templates (
    room_id SERIAL PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    room_type VARCHAR(50) NOT NULL,
    accessible VARCHAR NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    room_details TEXT
);
INSERT INTO room_templates (room_number, room_type, accessible, price, room_details)
VALUES
('455', 'Single', 'true', 120.00, 'Wi-Fi, TV'),
('723', 'Double', 'false', 180.00, 'Wi-Fi, Safe'),
('299', 'Family', 'true', 250.00, 'Wi-Fi, TV, Refreshments, Radio');
