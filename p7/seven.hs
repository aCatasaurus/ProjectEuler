-- What is the 10,001st prime number?

main = print . nthprime $ (10001 :: Integer)


nthprime :: Integral i => i -> i
nthprime n = head (nprimes n 0 [])


nprimes :: Integral i => i -> i -> [i] -> [i]
nprimes n l primes
    | l == 0    = nprimes n 1 [2]
    | l < n     = nprimes n (l + 1) (extendprimes (head primes) primes)
    | otherwise = primes


extendprimes :: Integral i => i -> [i] -> [i]
extendprimes x (prime:primes)
    | relprime x (prime:primes) = (x:prime:primes)
    | otherwise                 = extendprimes (x + 1) (prime:primes)


relprime :: Integral i => i -> [i] -> Bool
relprime n ps = all (\p -> n `mod` p /= 0) ps
