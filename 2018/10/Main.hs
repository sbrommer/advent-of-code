module Main where

import Data.List.Split (splitOn)
import Data.List.Tools (dropUntil)
import Data.Tuple.Extra (both)
import Control.Arrow ((&&&))

type Light = (Position, Velocity)
type Position = (Int, Int)
type Velocity = (Int, Int)

main :: IO()
main = do
    contents <- readFile "input.txt"
    putStrLn $ part1and2 $ parse contents

parse :: String -> [Light]
parse = map parseLine . lines

parseLine :: String -> Light
parseLine line = both (both read) ((px, py), (vx, vy))
    where
        line'    = dropUntil ('<' ==) line
        [px, py] = splitOn ", " $ takeWhile ('>' /=) line'
        [vx, vy] = splitOn ", " $ takeWhile ('>' /=) $ dropUntil ('<' ==) line'

part1and2 :: [Light] -> String
part1and2 = show' . closest . zip [0..] . iterate move

move :: [Light] -> [Light]
move = map move'
    where
        move' :: Light -> Light
        move' ((px, py), v@(vx, vy)) = ((px + vx, py + vy), v)

closest :: [(Int, [Light])] -> (Int, [Light])
closest (state1:state2:states)
    | isClosest = state1
    | otherwise = closest $ state2:states
    where
        isClosest = width (snd state1) < width (snd state2)

width :: [Light] -> Int
width lights = py - px
    where
        ((px, py), _) = range $ map fst lights

range :: [Position] -> ((Int, Int), (Int, Int))
range positions = ((minimum xs, maximum xs), (minimum ys, maximum ys))
    where
        xs = map fst positions
        ys = map snd positions

show' :: (Int, [Light]) -> String
show' (t, lights) =
    let
        positions = map fst lights
        ((minx, maxx), (miny, maxy)) = range positions
    in
        unlines $
        show t :
        [[if (x, y) `elem` positions then '#' else '.'
        | x <- [minx .. maxx]]
        | y <- [miny .. maxy]]
