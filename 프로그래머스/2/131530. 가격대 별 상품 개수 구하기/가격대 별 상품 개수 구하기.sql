SELECT FLOOR(PRICE/10000) * 10000 PRICE_GROUP, COUNT(*) PRODUCTS FROM PRODUCT GROUP BY FLOOR(PRICE/10000) ORDER BY PRICE_GROUP;