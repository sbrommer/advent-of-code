module Main where

import Data.List.Split (splitOn)
import Data.Set (Set, fromList, size, unions, intersection)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [[Set Char]]
parse = map parseGroup . splitOn "\n\n"

parseGroup :: String -> [Set Char]
parseGroup = map fromList . lines

part1 :: [[Set Char]] -> Int
part1 = sum . map (size . unions)

part2 :: [[Set Char]] -> Int
part2 = sum . map (size . intersections)

intersections :: Ord a => [Set a] -> Set a
intersections = foldl1 intersection
