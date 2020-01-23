module Main where

import Data.Char (toUpper, toLower, isLower)
import Data.List (sort, nub)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> String
parse = head . lines

part1 :: String -> Int
part1 = length . reduce

part2 :: String -> Int
part2 ps =
      minimum
    $ map (\t -> part1 $ deleteType t ps')  -- Delete types, calculate reduced length
    $ nub $ map toLower ps'                 -- Compute types
    where
      ps' = reduce ps                       -- Pre-reduce string

reduce :: String -> String
reduce = foldr reduce' ""

reduce' :: Char -> String -> String
reduce' p (q:qs) | reacts p q = qs
reduce' p qs = p:qs

reacts :: Char -> Char -> Bool
reacts p q = p /= q && toLower p == toLower q

deleteType :: Char -> String -> String
deleteType t = filter ((/=) t . toLower)
