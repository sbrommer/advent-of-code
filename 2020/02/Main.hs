module Main where

import Data.List.Split (splitOn)
import Data.List.Utils (countElem)
import Data.Ord.HT (inRange)
import Control.Arrow ((&&&))

data Policy = Policy Int Int Char

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [(Policy, String)]
parse = map parseLine . lines

parseLine :: String -> (Policy, String)
parseLine line =
    let [ns, c, pw] = words line
        [n1, n2] = map read $ splitOn "-" ns
    in (Policy n1 n2 $ head c, pw)

part1 :: [(Policy, String)] -> Int
part1 = length . filter (uncurry isValid1)

part2 :: [(Policy, String)] -> Int
part2 = length . filter (uncurry isValid2)

isValid1 :: Policy -> String -> Bool
isValid1 (Policy n1 n2 c) pw = inRange (n1, n2) $ c `countElem` pw

isValid2 :: Policy -> String -> Bool
isValid2 (Policy n1 n2 c) pw = (pw !! (n1 - 1) == c) /= (pw !! (n2 - 1) == c)
