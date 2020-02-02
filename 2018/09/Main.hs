module Main where

import Data.List.PointedList.Circular
import Data.IntMap as M (IntMap, insertWith, empty)
import Data.Tuple.Extra (both)
import Data.Tuple.Lazy (mapSnd)
import Data.Maybe (fromJust)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> (Int, Int)
parse = both read . ((!! 0) &&& (!! 6)) . words . head . lines

part1 :: (Int, Int) -> Int
part1 (nplayers, lastmarble) =
    maximum $ snd $ foldl (play nplayers) (singleton 0, empty) [1 .. lastmarble]

part2 :: (Int, Int) -> Int
part2 = part1 . mapSnd (* 100)

play :: Int -> (PointedList Int, IntMap Int) -> Int -> (PointedList Int, IntMap Int)
play nplayers game@(_, _) marble -- Somehow, if I don't add the @(_,_), I get a stack overflow...
    | marble `mod` 23 == 0 = playForPoints nplayers game marble
    | otherwise            = playNormal    nplayers game marble

playNormal :: Int -> (PointedList Int, IntMap Int) -> Int -> (PointedList Int, IntMap Int)
playNormal nplayers (marbles, points) marble = (marbles', points)
    where
        marbles' = insertRight marble $ next marbles

playForPoints :: Int -> (PointedList Int, IntMap Int) -> Int -> (PointedList Int, IntMap Int)
playForPoints nplayers (marbles, points) marble = (marbles'', points')
    where
        marbles'  = moveN (-7) marbles                              -- Move 7 to the left
        removed   = _focus marbles'                                 -- Get marble to remove
        marbles'' = fromJust $ deleteRight marbles'                 -- Remove marble
        player    = marble `mod` nplayers                           -- Determine player
        points'   = insertWith (+) player (marble + removed) points -- Add points to player
