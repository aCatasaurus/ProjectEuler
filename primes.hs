
isprime :: Integral n => n -> n
isprime n =

primes :: (Integral n, Integral p) => n -> [p]
primes n = take n primeGen

primeGen :: Integral p => [p]
primeGen
    |
    where n = 2
