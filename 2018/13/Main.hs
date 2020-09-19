{-# LANGUAGE TupleSections #-}

module Main where

import Prelude as P
import Data.Map as M
import Data.List (sort, scanl, find)
import Data.List.Tools (dropUntil)
import Data.Tuple.Lazy (mapPair)
import Data.Tuple.Extra (both)
import Data.Maybe (isJust, fromJust)
import Control.Arrow ((&&&))

type Coord = (Int, Int)
data System = System {track :: Map Coord Char, carts :: Map Coord Cart}
type Cart   = (Char, Char)

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> System
parse = toSystem . fromList . concatMap parseLine . zip [0 ..] . lines

parseLine :: (Int, String) -> [((Int, Int), Char)]
parseLine (y, line) = [((x, y), c) | (x, c) <- zip [0 ..] line]

toSystem :: Map Coord Char -> System
toSystem map = System track carts
    where
        carts = M.map (, 'L') $ M.filter (`elem` ['>', '<', '^', 'v']) map
        track = M.map under map
        under c | c `elem` ['>', '<'] = '-'
                | c `elem` ['^', 'v'] = '|'
                | otherwise           = c

part1 :: System -> Coord
part1 = fromJust . head . dropUntil isJust . P.map collision . steps
    where
        collision = fmap fst . find ((==) 'x' . fst . snd) . toList . carts

part2 :: System -> Coord
part2 = head . keys . carts . head . P.filter oneCart . iterate tick
    where
        oneCart = ((==) 1 . size) . carts

steps :: System -> [System]
steps system = systems ++ steps (last systems)
    where
        systems = scanl (step False) system $ coords system

tick :: System -> System
tick system = P.foldl (step True) system $ coords system

coords :: System -> [Coord]
coords = sort . M.keys . carts

step :: Bool -> System -> Coord -> System
step clean (System track carts) coord = System track newCarts
    where
        oldCart   = carts ! coord
        newCoord  = nextCoord oldCart coord
        square    = track ! newCoord
        collision = newCoord `member` carts

        newCart   | collision && not clean = ('x', undefined)
                  | otherwise              = nextCart oldCart square

        newCarts  | coord `notMember` carts = carts -- When it collided and was cleaned earlier.
                  | collision && clean      = delete newCoord         $ delete coord carts
                  | otherwise               = insert newCoord newCart $ delete coord carts

moves :: Map Char Coord
moves = fromList [ ('>', ( 1,  0))
                 , ('<', (-1,  0))
                 , ('^', ( 0, -1))
                 , ('v', ( 0,  1))
                 , ('x', ( 0,  0))]

nextCoord :: Cart -> Coord -> Coord
nextCoord (c, _) coord = addTuples coord $ moves ! c

addTuples :: Num a => (a, a) -> (a, a) -> (a, a)
addTuples t1 = mapPair (both (+) t1)

turnRight :: Char -> Char
turnRight c
    | c == '>' = 'v'
    | c == 'v' = '<'
    | c == '<' = '^'
    | c == '^' = '>'

turnLeft :: Char -> Char
turnLeft c
    | c == '>' = '^'
    | c == 'v' = '>'
    | c == '<' = 'v'
    | c == '^' = '<'

nextCart :: (Char, Char) -> Char -> (Char, Char)
nextCart (c, t) s = (c', t')
    where
        c' | s == '+'  &&  t == 'R' = turnRight c
           | s == '+'  &&  t == 'L' = turnLeft  c
           | s == '/'  && (c == '<' || c == '>') = turnLeft  c
           | s == '/'  && (c == '^' || c == 'v') = turnRight c
           | s == '\\' && (c == '<' || c == '>') = turnRight c
           | s == '\\' && (c == '^' || c == 'v') = turnLeft  c
           | otherwise = c
        t' | s == '+'  &&  t == 'S' = 'R'
           | s == '+'  &&  t == 'R' = 'L'
           | s == '+'  &&  t == 'L' = 'S'
           | otherwise = t
