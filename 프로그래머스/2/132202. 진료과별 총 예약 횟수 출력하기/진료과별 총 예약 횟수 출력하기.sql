select mcdp_cd as "진료과코드", count(mcdp_cd) as "5월예약건수"
from appointment
where apnt_ymd between '2022-05-01' and '2022-05-31'
group by mcdp_cd
order by COUNT(MCDP_CD) ASC, MCDP_CD ASC
