-- a SQL script that creates a trigger that decrease
-- s the quantity of an item after adding a new order.
CREATE TRIGGER decrease_qty AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;