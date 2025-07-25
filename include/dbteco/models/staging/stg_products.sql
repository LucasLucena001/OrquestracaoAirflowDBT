{{ config(materialized='view') }}

select
  product_id,
  initcap(product_name) as product_name,
  lower(category) as category,
  cast(price as numeric(10,2)) as price
from {{ ref('raw_products') }}
