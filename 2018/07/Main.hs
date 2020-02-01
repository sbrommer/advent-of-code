{-# LANGUAGE TupleSections #-}

module Main where

import Prelude as P
import Data.Char (ord)
import Data.List.Split (splitOn)
import Data.List.Extra (minimumOn)
import Data.Tuple.Extra (both)
import Data.Tuple.Lazy (mapSnd)
import Data.Set as S (Set, toList, fromList, singleton, union, unions, empty, delete, map)
import Data.Map as M (Map, toList, fromList, fromListWith, keys, elems, union, filter, delete, map)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> Map Char (Set Char)
parse contents = reqs `M.union` noreqs
    where
        reqs   = fromListWith S.union $ P.map parseLine $ lines contents
        steps  = unions $ S.fromList (keys reqs) : elems reqs
        noreqs = M.fromList $ S.toList $ S.map (, empty) steps

parseLine :: String -> (Char, Set Char)
parseLine = mapSnd singleton . both head . ((!! 7) &&& (!! 1)) . splitOn " "

part1 :: Map Char (Set Char) -> String
part1 reqs = steps1 reqs ""

steps1 :: Map Char (Set Char) -> String -> String
steps1 reqs steps
    | null reqs = reverse steps
    | otherwise = steps1 reqs' (step:steps)
        where
            step  = minimum $ keys $ M.filter null reqs
            reqs' = M.map (step `S.delete`) $ step `M.delete` reqs

part2 :: Map Char (Set Char) -> Int
part2 reqs = steps2 reqs' pending 0
    where
        starting = keys $ M.filter null reqs
        reqs'    = foldr M.delete reqs starting
        pending  = M.fromList $ zipMap getTime starting

steps2 :: Map Char (Set Char) -> Map Char Int -> Int -> Int
steps2 reqs pending time
    | null pending = time
    | otherwise = steps2 reqs'' pending'' (time + wait)
        where
            -- Get step that is done first with waiting time.
            (step, wait) = minimumOn snd $ M.toList pending
            -- Delete this step from all requirements.
            reqs'        = M.map (step `S.delete`) reqs
            -- Update the waiting time for the remaining pending steps.
            pending'     = M.map (flip (-) wait) $ step `M.delete` pending
            -- Calculate how many new pending steps there can be.
            nToStart     = (-) 5 $ length pending'
            -- Get a Map of nToStart (steps, waiting times) that have no requirements left.
            ready        = M.fromList $ zipMap getTime $ take nToStart $ keys $ M.filter null reqs'
            -- Delete these ready steps from the requirements Map.
            reqs''       = foldr M.delete reqs' $ keys ready
            -- Add these ready steps to the pending Map.
            pending''    = ready `M.union` pending'

getTime :: Char -> Int
getTime c = ord c - ord 'A' + 61

zipMap :: (a -> b) -> [a] -> [(a, b)]
zipMap f xs = zip xs (P.map f xs)

count :: (a -> Bool) -> [a] -> Int
count p = go 0
  where go n [] = n
        go n (x:xs) | p x       = go (n+1) xs
                    | otherwise = go n xs
