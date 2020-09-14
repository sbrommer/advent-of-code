{-# LANGUAGE TupleSections #-}

module Main where

import Data.Tree
import Control.Arrow ((&&&))

type Metadata = [Int]
type Input = [Int]

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> Tree Metadata
parse = parseTree . map read . words

parseTree :: Input -> Tree Metadata
parseTree = head . fst . parseTree' . ([],)

parseTree' :: ([Tree Metadata], Input) -> ([Tree Metadata], Input)
parseTree' (siblings, c:m:input) = (tree : siblings, drop m input')
    where
        tree = Node (take m input') (reverse children)
        (children, input') = applyN c parseTree' ([], input)

part1 :: Tree Metadata -> Int
part1 = sum . fmap sum

part2 :: Tree Metadata -> Int
part2 tree@(Node metadata children)
    | null children = part1 tree
    | otherwise =
          sum
        $ map (part2 . (children !!) . subtract 1)
        $ filter (`inRange` (1, length children)) metadata

-- Helper functions
inRange :: Int -> (Int, Int) -> Bool
inRange n (l, h) = l <= n && n <= h

applyN :: Int -> (a -> a) -> a -> a
applyN n f x = iterate f x !! n

