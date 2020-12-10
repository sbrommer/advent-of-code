module Main where

import Data.List (sort)
import Data.List.Split (splitOn)

import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [Int]
parse = (\xs -> 0 : xs ++ [maximum xs + 3]) . map read . lines

part1 :: [Int] -> Int
part1 = uncurry (*) . (count 1 &&& count 3) . differences . sort

part2 :: [Int] -> Int
part2 xs = 2 ^ count 2 ones * 4 ^ count 3 ones * 7 ^ count 4 ones
    where
        ones = map length $ splitOn [3] $ differences $ sort xs

differences :: [Int] -> [Int]
differences xs = zipWith (-) (tail xs) xs

count :: Eq a => a -> [a] -> Int
count x = length . filter (x ==)
