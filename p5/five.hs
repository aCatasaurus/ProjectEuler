
-- module Five where

main = print . lcm_up_to $ (20 :: Integer)


-- using built in lcm
-- lcm_up_to :: Integral i => i -> i
-- lcm_up_to n = foldr (lcm) n [2..n - 1]


-- using Euclid's algorithm
-- lcm_up_to :: Integral i => i -> i
-- lcm_up_to n = foldr (my_lcm) n [2..n - 1]
--
-- my_lcm :: Integral i => i -> i -> i
-- my_lcm a b = a * (b `div` (euclids a b))
--
-- euclids :: Integral i => i -> i -> i
-- euclids a 0 = a
-- euclids a b = euclids b (a `mod` b)


-- using iterative list approach
lcm_up_to :: Integral i => i -> i
lcm_up_to n = foldr (*) 1 (factors [2..n])

factors :: Integral i => [i] -> [i]
factors []      = []
factors (x:xs)  = [x] ++ (factors [if n `mod` x == 0 then n `div` x else n | n <- xs])
