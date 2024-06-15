with raw_data as (
    select
        cast(id as bigint) as id,
        cast(date as timestamp) as date,
        message,
        cast(sender_id as bigint) as sender_id,
        cast(views as int) as views
        time_of_day,
        cast(post_hour as int) as post_hour,
        channel_name
    from {{ ref('data_raw')}}
)

select * from raw_data