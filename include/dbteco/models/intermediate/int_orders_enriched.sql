{{ config(materialized='view') }}

select
  o.order_id,
  o.customer_id,
  c.first_name,
  c.last_name,
  c.email,
  o.order_date,
  o.status,
  p.payment_method,
  p.amount as payment_amount,
  p.payment_date
from {{ ref('stg_orders') }} o
left join {{ ref('stg_customers') }} c on o.customer_id = c.customer_id
left join {{ ref('stg_payments') }} p on o.order_id = p.order_id
