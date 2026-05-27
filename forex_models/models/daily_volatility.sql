with source as (
    select * from eur_usd
),

ranked as (
    select
        date,
        daily_range,
        rank() over (order by daily_range desc) as volatility_rank
    from source
)

select * from ranked
order by volatility_rank
limit 10