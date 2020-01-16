module Main where

import Data.List (group, sort, find)
import Data.Function (on)
import Data.Maybe (catMaybes, fromJust)
import Control.Applicative (liftA2)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ lines contents

part1 :: [String] -> Int
part1 ids = count (elem 2) letterCounts * count (elem 3) letterCounts
    where
        letterCounts = map (map length . group . sort) ids

part2 :: [String] -> String
part2 =
      fromJust
    . fmap (catMaybes . uncurry (zipWith justEqual))              -- Compute common chars.
    . find ((==) 1 . sum . map bool2int . uncurry (zipWith (/=))) -- Find where dif is 1.
    . uncurry (liftA2 (,))                                        -- Make cartesian product.
    . dupe

count :: (a -> Bool) -> [a] -> Int
count p = length . filter p

bool2int :: Bool -> Int
bool2int True = 1
bool2int _    = 0

dupe :: a -> (a, a)
dupe a = (a, a)

justEqual :: Eq a => a -> a -> Maybe a
justEqual a b
    | a == b    = Just a
    | otherwise = Nothing
