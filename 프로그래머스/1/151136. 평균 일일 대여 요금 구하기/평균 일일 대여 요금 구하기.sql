select round(avg(daily_fee),0) AS AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV';