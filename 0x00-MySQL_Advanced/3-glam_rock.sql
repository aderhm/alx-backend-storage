-- This script lists all bands with Glam rock as their main style, ranked by their longevity.

-- List bands with Galm rock as their style
SELECT band_name, (COALESCE(split, 2022) - formed) as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
