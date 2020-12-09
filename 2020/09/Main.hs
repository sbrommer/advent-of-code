module Main where

import Data.List (tails, find)
import Data.Maybe (fromJust)

import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [Int]
parse = map read . lines

part1 :: [Int] -> Int
part1 = findInvalid

findInvalid :: [Int] -> Int
findInvalid =
    fst . fromJust . find (uncurry notElem) .
    uncurry zip . (drop 25 &&& map combinationSums . windows)

windows :: [Int] -> [[Int]]
windows = map (take 25) . tails

combinationSums :: [Int] -> [Int]
combinationSums xs = [x + y | x <- xs, y <- xs, x < y]

part2 :: [Int] -> Int
part2 xs = uncurry (+) $ (minimum &&& maximum) $ contiguousSet (findInvalid xs) xs

contiguousSet :: Int -> [Int] -> [Int]
contiguousSet n = go . splitAt 25
    where
        go :: ([Int], [Int]) -> [Int]
        go (window, rest)
            | s == n = window
            | s <  n = go (window ++ [head rest], tail rest)
            | s >  n = go (tail window, rest)
            where
                s = sum window

