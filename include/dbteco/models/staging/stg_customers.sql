{{ config(materialized='view') }}

select
  customer_id,
  lower(trim(first_name)) as first_name,
  lower(trim(last_name)) as last_name,
  lower(email) as email,
  cast(created_at as date) as created_at
from {{ ref('raw_customers') }}
