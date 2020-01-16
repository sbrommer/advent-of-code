module Main where

import Data.List.Split (splitOn)
import Data.Map (elems, fromListWith)
import Data.Set (Set, size, (\\), union, unions, singleton, toList)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [[Int]]
parse = map parseLine . lines

parseLine :: String -> [Int]
parseLine line = map read [tail i, x, init y, w, h]
    where
        [i, _, pos, dims] = splitOn " " line
        [x, y]            = splitOn "," pos
        [w, h]            = splitOn "x" dims

part1 :: [[Int]] -> Int
part1 = length . overlapping . fabric

part2 :: [[Int]] -> Int
part2 =
      head . toList                                               -- Change type from Set Int to Int
    . uncurry (\\) . (unions &&& (unions . overlapping)) . fabric -- Calculate answer

fabric :: [[Int]] -> [Set Int]
fabric =
      elems
    . fromListWith union
    . concatMap (\[i, x, y, w, h] -> [ ((x', y'), singleton i)
                                     | x' <- take w [x..],
                                       y' <- take h [y..]])

overlapping :: [Set Int] -> [Set Int]
overlapping = filter ((> 1) . size)
