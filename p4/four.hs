
-- Find the largest palindrome made from the product of two 3-digit numbers.

main = print . showPair . maxPair . palindromes $ (3 :: Integer)

gtPair :: Integral i => (i, i) -> (i, i) -> (i, i)
gtPair x y
    | fst x * snd x > fst y * snd y = x
    | otherwise                     = y

maxPair :: Integral i => [(i, i)] -> (i, i)
maxPair ps = foldr gtPair (0, 0) ps

showPair :: (Show i) => (i, i) -> [Char]
showPair (a, b) = show a ++ " " ++ show b

palindromes :: Integral i => i -> [(i, i)]
palindromes n = [(n, n), (n + 1, n + 1)]
