module Main where

import Prelude as P
import Data.Sequence as S
import Data.Char (digitToInt, intToDigit)
import Data.List.Utils (subIndex)
import Data.Maybe (fromJust)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> String
parse = head . lines

recipes :: [Int]
recipes = 3 : 7 : improve 0 1 (fromList [3, 7])

improve :: Int -> Int -> Seq Int -> [Int]
improve elf1 elf2 recipes = scores ++ improve elf1' elf2' recipes'
    where
        score1 = recipes `index` elf1
        score2 = recipes `index` elf2
        scores = map digitToInt $ show $ score1 + score2
        recipes' = recipes >< fromList scores
        elf1' = (elf1 + score1 + 1) `mod` S.length recipes'
        elf2' = (elf2 + score2 + 1) `mod` S.length recipes'

part1 n = map intToDigit $ P.take 10 $ P.drop (read n) recipes
part2 n = fromJust $ subIndex (map digitToInt n) recipes
