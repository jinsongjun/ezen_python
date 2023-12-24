use ezen2;

select * from emp;

## SAL가 2000보다 높은 사람의 정보를 출력 
select * from emp where SAL > 2000;

## JOB이 MANAGER인 사람의 데이터를 조회
select * from emp where JOB = "MANAGER";

## 차순정렬 변경 
## SAL컬럼의 내림차순 정렬 
select * from emp order by SAL desc;
## NAME을 기준으로 오름차순 정렬
select * from emp order by ENAME; 

## ENAME이 특정 문자로 시작하는 데이터만 조회 
select * from emp where ENAME LIKE 'M%';

select * from emp where ENAME LIKE '%S';

select * from emp where ENAME LIKE '%A%';

## select 구문에 연산자를 사용하는 방법
select 
ENAME as '이름' , 
SAL as '월급', 
SAL*12 as '연봉' 
from emp; 

## 논리연산자 사용법 ( AND, OR )
## JOB이 SALESMAN이고 SAL가 1500이상인 사람을 조회
select * from emp 
where JOB = 'SALESMAN' AND SAL >= 1500;

## JOB이 SALESMAN이거나 MANAGER인 사람을 조회
select * from emp 
where JOB = 'SALESMAN' OR JOB = 'MANAGER';
select * from emp 
where JOB in ('SALESMAN', 'MANAGER');

## between 연산자
select * from emp where SAL between 2000 AND 3000;  
select * from emp where SAL not between 2000 AND 3000;

## 중복데이터를 제거하고 표시 
select distinct DEPTNO from emp;

## table의 결합
## 유니언 결합 

## 조인 결합  
select * from 
emp LEFT JOIN dept 
ON emp.deptno = dept.deptno
where emp.DEPTNO = 20;

## 서브쿼리문 예시 
## 조인결합을 한 데이터에서 LOC가 'NEW YORK'인 데이터를 조회 
select * from 
emp left join dept
on emp.DEPTNO = dept.DEPTNO
where LOC = 'NEW YORK';
## 서브쿼리문으로 작성
# 부서의 지역이 DALLAS인 부서 번호를 조회 
select DEPTNO 
from dept 
where LOC = 'DALLAS';

select * from emp where DEPTNO in (20);

select * from 
emp 
where DEPTNO in (
select DEPTNO 
from dept 
where LOC != 'DALLAS');
