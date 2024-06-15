with channel_data as(
    select
        distinct
        dense_rank() over (order by channel_name) as channel_id,
        channel_name
    from {{ ref('fact_messages') }}
)

select * from channel_data