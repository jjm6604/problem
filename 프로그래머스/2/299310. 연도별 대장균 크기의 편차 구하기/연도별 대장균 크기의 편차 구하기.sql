SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, T2.MAX_SIZE - T1.SIZE_OF_COLONY AS YEAR_DEV, ID FROM ECOLI_DATA T1 JOIN (SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE FROM ECOLI_DATA GROUP BY YEAR(DIFFERENTIATION_DATE)) T2 ON YEAR(T1.DIFFERENTIATION_DATE) = T2.YEAR ORDER BY YEAR, YEAR_DEV;

# SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE FROM ECOLI_DATA GROUP BY YEAR(DIFFERENTIATION_DATE);