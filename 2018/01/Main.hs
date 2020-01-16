module Main where

import Data.List     (scanl', find)
import Data.IntSet   (member, insert, empty)
import Data.Maybe    (fromJust)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [Int]
parse = map parseLine . lines

parseLine :: String -> Int
parseLine ('+':cs) = read cs
parseLine cs       = read cs

part1 :: [Int] -> Int
part1 = sum

part2 :: [Int] -> Int
part2 =
      fromJust
    . fmap fst
    . find (uncurry member)                 -- Find when freq is already in freq history set.
    . (zip <*> scanl' (flip insert) empty)  -- Create freq history sets; zip with freq list.
    . scanl' (+) 0                          -- Compute frequency list.
    . cycle                                 -- Cycle the changes list.
