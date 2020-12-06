module Main where

import Data.Set (fromList, toList, (\\))
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [Int]
parse = map binToDec . lines

binToDec :: String -> Int
binToDec = go 0
    where
        go :: Int -> String -> Int
        go acc ""     = acc
        go acc (c:cs) = go (2 * acc + fromEnum (c `elem` "BR")) cs

part1 :: [Int] -> Int
part1 = maximum

part2 :: [Int] -> Int
part2 ids = head $ toList $ fromList [minimum ids .. maximum ids] \\ fromList ids
