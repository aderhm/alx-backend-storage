-- This script creates an index idx_name_first on the table names and the first letter of name.

-- Add a column for the name first letter
ALTER TABLE names ADD name_first_letter CHAR(1) GENERATED ALWAYS AS (SUBSTRING(name, 1, 1)) STORED;
-- Create idx_name_first
CREATE INDEX idx_name_first ON names (name_first_letter);
