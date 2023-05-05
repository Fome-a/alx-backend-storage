-- a SQL script that creates an index 
-- the table of names and the first letter of the name.
CREATE INDEX idx_name_first ON names(name(1))