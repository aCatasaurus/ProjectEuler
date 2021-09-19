-- The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
--
-- Find the sum of all the primes below two million.

bound :: Integer
bound = 10


main :: IO ()
main = print . sum $ primesupto bound


primesupto :: Integral i => i -> [i]
primesupto n = getprimesupto n []


getprimesupto :: Integral i => i -> [i] -> [i]
getprimesupto n [] = getprimesupto n (extendprimes 3 [2])
getprimesupto n (p:ps)
    | n > p     = getprimesupto n (extendprimes (p + 1) (p:ps))
    | otherwise = ps


extendprimes :: Integral i => i -> [i] -> [i]
extendprimes x primes
    | relprime x primes = (x:primes)
    | otherwise         = extendprimes (x + 1) primes


relprime :: Integral i => i -> [i] -> Bool
relprime n ps = all (\p -> n `mod` p /= 0) ps


-- import Data.Vector.Mutable as Vlib
-- type Vec = Vlib.MVector
--
--
-- bound :: Int
-- bound = 100
--
--
-- main :: IO ()
-- main = print $ esieve bound
--
--
-- esieve :: Integral i => i -> Vec Bool
-- esieve n = sieve n 0 0 (Vlib.replicate bound True)
--
--
-- sieve :: Integral i => i -> i -> i -> Vec Bool -> Vec Bool
-- sieve n 0 0 a = sieve n 2 0 a
-- sieve n i 0 a
--     | i > root  = a
--     | otherwise = sieve n i (i * i) a
--     where root = ceiling . sqrt $ n
-- sieve n i j a
--     | j > n     = sieve n (i + 1) 0 a
--     | otherwise = (Vlib.write a j False) >> (sieve n i (j + i) a)
