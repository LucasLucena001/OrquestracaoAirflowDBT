{{ config(materialized='table') }}

select
  o.order_id,
  o.customer_id,
  c.email as customer_email,
  o.order_date,
  o.status,
  o.payment_method,
  o.payment_amount,
  oi.total_items,
  oi.total_order_value
from {{ ref('int_orders_enriched') }} o
left join (
    select
      order_id,
      count(*) as total_items,
      sum(total_item_value) as total_order_value
    from {{ ref('int_order_items_enriched') }}
    group by order_id
) oi on o.order_id = oi.order_id
left join {{ ref('stg_customers') }} c on o.customer_id = c.customer_id
