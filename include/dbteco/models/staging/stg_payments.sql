{{ config(materialized='view') }}

select
  payment_id,
  order_id,
  lower(payment_method) as payment_method,
  cast(amount as numeric(10,2)) as amount,
  cast(payment_date as date) as payment_date
from {{ ref('raw_payments') }}
