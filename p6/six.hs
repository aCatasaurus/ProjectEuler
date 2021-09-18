-- Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

main = print . f $ (100 :: Integer)

f :: Integral i => i -> i
f n = n * (n + 1) `div` 2 * (n * (n + 1) `div` 2 - (2 * n + 1) `div` 3)


-- S1 = sum(x  , 1, n) = n(n + 1) / 2
-- S2 = sum(x^2, 1, n) = n(n+1)(2n+1)/6
-- S1^2 - S2 = n(n + 1) / 2 * (n(n + 1) / 2 - (2n + 1) / 3)
