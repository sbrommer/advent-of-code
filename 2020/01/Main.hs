module Main where

import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [Int]
parse = map read . lines

part1 :: [Int] -> Int
part1 xs = head [x * y | x <- xs, y <- xs, x + y == 2020]

part2 :: [Int] -> Int
part2 xs = head [x * y * z | x <- xs, y <- xs, z <- xs, x + y + z == 2020]
