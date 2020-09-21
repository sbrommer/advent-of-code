module Main where

import Prelude as P
import Data.Map as M
import Data.List (intercalate)
import Data.List.Utils (countElem)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> Map (Int, Int) Char
parse = fromList . concatMap parseLine . zip [0 ..] . lines

parseLine :: (Int, String) -> [((Int, Int), Char)]
parseLine (y, line) = [((x, y), c) | (x, c) <- zip [0 ..] line]

adjacent :: (Int, Int) -> [(Int, Int)]
adjacent (x, y) = [ (x', y')
                  | x' <- [x-1 .. x+1]
                  , y' <- [y-1 .. y+1]
                  , (x', y') /= (x, y)]

showArea :: Map (Int, Int) Char -> String
showArea area =
    intercalate "\n" [[ area ! (x, y) | x <- [0 .. w]] | y <- [0 .. h]]
    where
        w = maximum $ P.map fst $ keys area
        h = maximum $ P.map snd $ keys area

step :: Map (Int, Int) Char -> Map (Int, Int) Char
step area = mapWithKey (step1 area) area

step1 :: Map (Int, Int) Char -> (Int, Int) -> Char -> Char
step1 area coord acre
    | acre == '.' &&  nTree   >= 3                = '|'
    | acre == '|' &&  nLumber >= 3                = '#'
    | acre == '#' && (nLumber <= 0 || nTree <= 0) = '.'
    | otherwise = acre
    where
        coords  = P.filter (`M.member` area) $ adjacent coord
        acres   = P.map (area !) coords
        nTree   = countElem '|' acres
        nLumber = countElem '#' acres

score :: Map (Int, Int) Char -> Int
score area =
    let acres = elems area
    in  countElem '|' acres * countElem '#' acres

part1 :: Map (Int, Int) Char -> Int
part1 = score . flip (!!) 10 . iterate step

-- Visual inspection shows that at score 169472, we start a 28-long loop.
part2 :: Map (Int, Int) Char -> Int
part2 area = loop !! ((1000000000 - length preLoop) `mod` 28)
    where
        scores  = P.map score $ iterate step area
        preLoop = P.takeWhile (169472 /=) scores
        loop    = P.take 28 $ P.dropWhile (169472 /=) scores
