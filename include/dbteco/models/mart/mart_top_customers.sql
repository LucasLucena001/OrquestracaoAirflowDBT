{{ config(materialized='table') }}

select
  o.customer_id,
  c.full_name,
  c.email,
  count(distinct o.order_id) as total_pedidos,
  sum(o.payment_amount) as total_gasto
from {{ ref('fct_orders') }} o
left join {{ ref('dim_customers') }} c
  on o.customer_id = c.customer_id
where o.status = 'completed'
group by o.customer_id, c.full_name, c.email
order by total_gasto desc
limit 10
