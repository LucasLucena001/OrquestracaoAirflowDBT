{{ config(materialized='table') }}

select
  customer_id,
  initcap(first_name) || ' ' || initcap(last_name) as full_name,
  email,
  created_at
from {{ ref('stg_customers') }}
