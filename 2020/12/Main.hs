module Main where

import Prelude as P
import Data.Map as M
import Linear

import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

-- Parse
parse :: String -> [(Char, Int)]
parse = P.map parseLine . lines

parseLine :: String -> (Char, Int)
parseLine = head &&& read . tail

-- Sulution
part1 :: [(Char, Int)] -> Int
part1 = manhattan . snd . P.foldl move1 (V2 0 1, V2 0 0)

move1 :: (V2 Int, V2 Int) -> (Char, Int) -> (V2 Int, V2 Int)
move1 (w, s) (a, v) =
    case a of
        'R' -> (turn v w, s)
        'L' -> (turn (360 - v) w, s)
        'F' -> (w, s + v *^ w)
        _   -> (w, s + v *^ dir a)

part2 :: [(Char, Int)] -> Int
part2 = manhattan . snd . P.foldl move2 (V2 1 10, V2 0 0)

move2 :: (V2 Int, V2 Int) -> (Char, Int) -> (V2 Int, V2 Int)
move2 (w, s) (a, v) =
    case a of
        'R' -> (turn v w, s)
        'L' -> (turn (360 - v) w, s)
        'F' -> (w, s + v *^ w)
        _   -> (w + v *^ dir a, s)

-- Helper functions
dir :: Char -> V2 Int
dir 'N' = V2 1 0
dir 'E' = V2 0 1
dir 'S' = V2 (-1) 0
dir 'W' = V2 0 (-1)

turn :: Int -> V2 Int -> V2 Int
turn d (V2 x y) =
    case d of
         90  -> V2 (-y) x
         180 -> V2 (-x) (-y)
         270 -> V2 y    (-x)

manhattan :: V2 Int -> Int
manhattan = sum . abs
