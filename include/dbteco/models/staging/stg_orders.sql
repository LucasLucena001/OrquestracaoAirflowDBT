{{ config(materialized='view') }}

select
  order_id,
  customer_id,
  cast(order_date as date) as order_date,
  lower(status) as status
from {{ ref('raw_orders') }}
