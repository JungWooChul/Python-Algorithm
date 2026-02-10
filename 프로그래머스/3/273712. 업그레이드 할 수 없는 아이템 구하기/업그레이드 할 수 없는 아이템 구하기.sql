-- 코드를 작성해주세요
SELECT
    ITEM_ID, ITEM_NAME, RARITY
FROM 
    ITEM_INFO
WHERE
    ITEM_ID NOT IN (
        SELECT DISTINCT(PARENT_ITEM_ID)
        FROM ITEM_TREE I
        WHERE PARENT_ITEM_ID IS NOT NULL  # NULL 값은 DB에서 비교연산을 할 때 항상 UNKNOWN(FALSE) 값을 반환하기 때문에 NULL 이 존재하면 아무 결과도 확인할 수 없다
    )
ORDER BY ITEM_ID DESC