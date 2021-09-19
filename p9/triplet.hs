-- A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
-- a^2 + b^2 = c^2
--
-- For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
--
-- There exists exactly one Pythagorean triplet for which a + b + c = 1000.
-- Find the product abc.

type Triple = (Integer, Integer, Integer)

total :: Integer
total = 1000


main :: IO ()
main = print $ showans $ gettriplet gen


-- generates triples, (a, b, c), satisfying a < b < c, a + b + c = 1000
gen :: [Triple]
gen = [(a, b, total - a - b) | a <- [1..(total - 3) `div` 3], b <- [a + 1..(total - a - 1) `div` 2]]


gettriplet :: [Triple] -> Triple
gettriplet (t:ts)
    | a^2 + b^2 == c^2  = t
    | otherwise         = gettriplet ts
    where (a, b, c) = t


showans :: Triple -> [Char]
showans t = "The triple is " ++ show t ++ " with abc = " ++ show (a * b * c)
    where (a, b, c) = t
