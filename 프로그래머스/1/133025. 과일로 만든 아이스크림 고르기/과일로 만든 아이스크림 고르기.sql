-- 코드를 입력하세요 
SELECT FLAVOR
FROM (SELECT A.SHIPMENT_ID, A.FLAVOR, A.TOTAL_ORDER, B.INGREDIENT_TYPE # join 진행 시 컬럼명 재정의
      FROM (FIRST_HALF as A # AS로 테이블명 재정의
            JOIN ICECREAM_INFO as B
      ON a.FLAVOR = b.FLAVOR)
      WHERE TOTAL_ORDER > 3000 AND INGREDIENT_TYPE = 'fruit_based') favorite_fruit_based # 서브 쿼리 작성시 새롭게 생성된 테이블명 선언
ORDER BY TOTAL_ORDER DESC;
