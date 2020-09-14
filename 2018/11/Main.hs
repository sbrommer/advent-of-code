module Main where

import Prelude as P
import Data.Map as M
import Data.List.Extra (maximumOn)
import Data.Tuple.Extra (thd3)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> Int
parse = read . head . lines

cellPower :: Int -> (Int, Int) -> Int
cellPower serialNr (x, y) = (rackId * y + serialNr) * rackId `div` 100 `mod` 10 - 5
    where
        rackId = x + 10

summedAreaTable :: Int -> Map (Int, Int) Int
summedAreaTable serialNr = P.foldl (sumArea serialNr) initialSAT coordinates
    where
        initialSAT = fromList [((x, 0), 0) | x <- [0 .. 300]] `union`
                     fromList [((0, y), 0) | y <- [0 .. 300]]
        coordinates = [(x, y) | total <- [2 .. 600], x <- [1 .. 300], let y = total - x, 0 < y, y <= 300]

sumArea :: Int -> Map (Int, Int) Int -> (Int, Int) -> Map (Int, Int) Int
sumArea serialNr sat k@(x, y) = insert k power sat
    where
        power = cellPower serialNr k +
                sat ! (x-1, y)       +
                sat ! (x,   y-1)     -
                sat ! (x-1, y-1)

squareTotal :: Map (Int, Int) Int -> (Int, Int, Int) -> Int
squareTotal sat (x, y, s) =
    sat ! (x+s-1, y+s-1) -
    sat ! (x+s-1, y  -1) -
    sat ! (x  -1, y+s-1) +
    sat ! (x  -1, y  -1)

part1 :: Int -> (Int, Int, Int)
part1 serialNr = maximumOn (squareTotal sat) [(x, y, 3) | x <- [1 .. 298], y <- [1 .. 298]]
    where
        sat = summedAreaTable serialNr

part2 :: Int -> (Int, Int, Int)
part2 serialNr = maximumOn (squareTotal sat) [(x, y, s) | s <- [1 .. 300], x <- [1 .. 301-s], y <- [1 .. 301-s]]
    where
        sat = summedAreaTable serialNr
