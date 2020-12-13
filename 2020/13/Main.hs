module Main where

import Data.List (find, findIndices)
import Data.List.Split (splitOn)
import Data.List.Extra (minimumOn)
import Data.String.Utils (maybeRead)
import Data.Maybe (catMaybes, fromJust, isJust)

import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

-- Parse
parse :: String -> (Int, [Maybe Int])
parse = ((read . head) &&& (parseLine . last)) . lines

parseLine :: String -> [Maybe Int]
parseLine = map maybeRead . splitOn ","

-- Solution
part1 :: (Int, [Maybe Int]) -> Int
part1 (t, mIds) = id * wait t id
    where
        id  = minimumOn (wait t) ids
        ids = catMaybes mIds

wait :: Int -> Int -> Int
wait t id = id - (t `mod` id)

part2 :: (Int, [Maybe Int]) -> Int
part2 (_, mIds) = fst $ foldl findTime (100000000000000, 1) $ zip offsets ids
    where
        ids     = catMaybes mIds
        offsets = findIndices isJust mIds

findTime :: (Int, Int) -> (Int, Int) -> (Int, Int)
findTime (min, step) (offset, id) =
    let min'  = fromJust $ find (\t -> (t + offset) `mod` id == 0) [min, min + step ..]
    in  (min', step * id)
