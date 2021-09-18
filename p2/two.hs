
main = print . sum $ [a | n <- [1..], let a = fib n, a `mod` 2 == 0, a < 1000000]

fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)
