
module Three where

main = print . max_factor $ 600851475143

-- Factors out fac from num.
-- If fac is the only factor of num, returns num.
remove :: Integral i => i -> i -> i
remove num fac = if num > fac && num `mod` fac == 0 then
                     remove (num `div` fac) fac
                 else num

-- Integer square root function, rounding up.
isqrt :: Integral i => i -> i
isqrt n = ceiling . sqrt . fromIntegral $ n

-- Finds the largest prime factor of n.
max_factor :: Integral i => i -> i
max_factor n = foldl remove n (2:[3,5..isqrt n])
