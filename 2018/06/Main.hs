module Main where

import Data.List.Split (splitOn)
import Data.List (sort, nub, elemIndices)
import Data.Set (fromList, toList, difference)
import Data.Function ((&), on)
import Control.Arrow ((&&&))
import Data.Tuple.Extra (both)
import Debug.Trace

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> [(Int, Int)]
parse = map parseLine . lines

parseLine :: String -> (Int, Int)
parseLine =  both read . first2 . splitOn ", "

part1 :: [(Int, Int)] -> Int
part1 points = maximum areas
    where
        -- Distances from every point on the grid to every point on the grid.
        distances            = distanceGrid points
        -- Same distances, but specifically for border points.
        borderDistances      = concatMap (distances &) [head, last, map head, map last]
        -- Closest region per point on the grid.
        closestRegions       = map getRegion $ concat distances
        -- Closest region per point on the border.
        borderClosestRegions = map getRegion borderDistances
        -- All occuring regions on the grid.
        regions              = nub $ concat closestRegions
        -- All infinite regions (= all regions on the border).
        infiniteRegions      = nub $ concat $ filter isSingleton borderClosestRegions
        -- All finite regions (= {regions} / {infinite regions})
        finiteRegions        = toList $ (difference `on` fromList) regions infiniteRegions
        -- Areas of the finite regions
        areas                = map (\n -> length $ filter ([n] ==) closestRegions) finiteRegions

part2 :: [(Int, Int)] -> Int
part2 = count (< 10000) . map sum . concat . distanceGrid

getRegion :: [Int] -> [Int]
getRegion distances = elemIndices (minimum distances) distances

distanceGrid :: [(Int, Int)] -> [[[Int]]]
distanceGrid points = [[map (distanceTo (x, y)) points | x <- [lx .. hx]] | y <- [ly .. hy]]
    where
        ((lx, ly), (hx, hy)) = gridBounds points

distanceTo :: (Int, Int) -> (Int, Int) -> Int
distanceTo (x1, y1) (x2, y2) = abs (x2 - x1) + abs (y2 - y1)

gridBounds :: [(Int, Int)] -> ((Int, Int), (Int, Int))
gridBounds = (both minimum &&& both maximum) . unzip

-- Helper functions
first2 :: [a] -> (a, a)
first2 (x1:x2:xs) = (x1, x2)

count :: (a -> Bool) -> [a] -> Int
count p = go 0
  where go n [] = n
        go n (x:xs) | p x       = go (n+1) xs
                    | otherwise = go n xs

isSingleton :: [a] -> Bool
isSingleton = (==) 1 . length
