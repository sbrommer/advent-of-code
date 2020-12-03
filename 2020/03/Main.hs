module Main where

import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [[Int]]
parse = map parseLine . lines

parseLine :: String -> [Int]
parseLine = cycle . map (fromEnum . (==) '#')

trees :: [[Int]] -> (Int, Int) -> Int
trees ts (w, h) = sum [(ts !! h) !! w | (w, h) <- zip [0, w ..] [0, h .. length ts - 1]]

part1 :: [[Int]] -> Int
part1 ts = trees ts (3, 1)

part2 :: [[Int]] -> Int
part2 ts = product $ map (trees ts) [(1,1), (3,1), (5,1), (7,1), (1,2)]
