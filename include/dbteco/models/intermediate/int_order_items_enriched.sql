{{ config(materialized='view') }}

select
  i.order_item_id,
  i.order_id,
  o.customer_id,
  i.product_id,
  p.product_name,
  p.category,
  p.price as product_price,
  i.unit_price,
  i.quantity,
  i.unit_price * i.quantity as total_item_value
from {{ ref('stg_order_items') }} i
left join {{ ref('stg_orders') }} o on i.order_id = o.order_id
left join {{ ref('stg_products') }} p on i.product_id = p.product_id
