module Main where

import Prelude as P
import Data.List (sort, group, find)
import Data.List.Split (splitOn)
import Data.List.Extra (maximumOn, minimumOn, groupOn)
import Data.Ord (comparing)
import Data.Function (on)
import Data.Set as S (Set, singleton, toList, union)
import Data.IntMap as M (IntMap, toList, fromList, fromListWith, (!), map, filter, elems)
import Control.Arrow ((&&&))
import Data.Tuple.Lazy (mapSnd)
import Data.Maybe (fromJust)
import Debug.Trace

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ precomputation $ parse contents

-- Parse
parse :: String -> [(Int, [Int])]
parse = parse' . sort . lines

parse' :: [String] -> [(Int, [Int])]
parse' [] = []
parse' (line:lines) = (id, times) : parse' lines'
    where
        (timeLines, lines') = break isGuardLine lines
        id    = parseIdLine line
        times = P.map parseTimeLine timeLines

parseIdLine :: String -> Int
parseIdLine = read . tail . (!! 3) . splitOn " "

isGuardLine :: String -> Bool
isGuardLine = (==) "Guard" . (!! 2) . splitOn " "

parseTimeLine :: String -> Int
parseTimeLine line = read [line !! 15, line !! 16]

-- Compute answers
precomputation :: [(Int, [Int])] -> IntMap (IntMap Int)
precomputation =
      M.map sleepPerMinute
    . M.fromListWith (++)

sleepPerMinute :: [Int] -> IntMap Int
sleepPerMinute = M.fromList . P.map (head &&& length) . group . sort . minutesSleeping

minutesSleeping :: [Int] -> [Int]
minutesSleeping [] = []
minutesSleeping (tSleep:tWake:times) = [minute | minute <- [tSleep .. tWake-1]] ++ minutesSleeping times

--part1 :: IntMap (IntMap Int) -> Int
part1 input = guard * minute
    where
        minute = fst $ maximumOn snd $ M.toList $ input ! guard
        guard  = fst $ fromJust $ find ((==) maxMinutes . sum . snd) $ M.toList input
        maxMinutes = maximum $ elems $ M.map sum input

part2 =
      uncurry (*)
    . mapSnd fst
    . maximumOn (snd . snd)            -- Get sleepiest guard
    . M.toList
    . M.map (maximumOn snd . M.toList) -- Get sleepiest minute per guard
    . M.filter (not . null)            -- Filter not-sleeping guards
