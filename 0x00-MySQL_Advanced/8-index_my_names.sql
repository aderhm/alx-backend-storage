-- This script creates an index idx_name_first on the table names and the first letter of name.

ALTER TABLE names ADD name_first_letter CHAR(1) GENERATED ALWAYS AS (SUBSTRING(name, 1, 1)) STORED;
CREATE INDEX idx_name_first ON names (name_first_letter);
