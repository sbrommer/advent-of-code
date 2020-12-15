module Main where

import Prelude  as P
import Data.Map as M
import Data.Set as S
import Data.Char (isDigit, isHexDigit)
import Data.List.Split (splitOn)
import Data.List.Extra (splitAtEnd)
import Data.Tuple.Lazy (mapFst)

import Control.Arrow ((&&&))

type Passport = Map String String

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

-- Parse
parse :: String -> [Passport]
parse = P.map pPassport . splitOn [""] . lines -- WORDS SPLIT OP WHITESPACE NIET SLECHTS SPATIES

pPassport :: [String] -> Passport
pPassport = M.fromList . P.map pField . concatMap words

pField :: String -> (String, String)
pField = toTuple . splitOn ":"

-- Solution
part1 :: [Passport] -> Int
part1 = count allFields

allFields :: Passport -> Bool
allFields = isSubsetOf required . S.fromList . keys
    where
        required = S.fromList ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

part2 :: [Passport] -> Int
part2 = count (\p -> allFields p && validFields p)

validFields :: Passport -> Bool
validFields = all isValidField . M.toList

isValidField :: (String, String) -> Bool
isValidField (key, value) =
    case key of
         "byr" -> between 1920 2002 $ read value

         "iyr" -> between 2010 2020 $ read value

         "eyr" -> between 2020 2030 $ read value

         "hgt" -> let (hgt, units) = mapFst read $ splitAtEnd 2 value
                  in  case units of
                           "cm" -> between 150 193 hgt
                           "in" -> between  59  76 hgt
                           _    -> False

         "hcl" -> head value == '#' && all isHexDigit (tail value)

         "ecl" -> value `elem` ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

         "pid" -> length value == 9 && all isDigit value

         "cid" -> True

-- Helper functions
toTuple :: [a] -> (a, a)
toTuple (x:y:_) = (x ,y)

count :: (a -> Bool) -> [a] -> Int
count p = length . P.filter p

between :: Ord a => a -> a -> a -> Bool
between min max x = min <= x && x <= max
