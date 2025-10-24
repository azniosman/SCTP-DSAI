SELECT DISTINCT
    item_number,
    item_description,
    category,
    category_name,
    vendor_number,
    vendor_name,
    pack,
    bottle_volume_ml
FROM {{ source('iowa_liquor_sales', 'sales') }}