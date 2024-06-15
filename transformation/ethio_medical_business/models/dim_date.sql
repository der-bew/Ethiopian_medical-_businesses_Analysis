with date_data as (
  select
    distinct date as date_id,
    extract(day from date) as day,
    extract(dayofweek from date) as day_of_week,
    extract(month from date) as month,
    extract(year from date) as year
  from {{ ref('fact_messages') }}
)

select * from date_data
