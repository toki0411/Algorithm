select e.DEPT_ID, d.DEPT_NAME_EN, ROUND(AVG(e.SAL)) AS AVG_SAL from HR_EMPLOYEES e
join HR_DEPARTMENT d on d.DEPT_ID = e.DEPT_ID
group by e.DEPT_ID
order by AVG_SAL desc;