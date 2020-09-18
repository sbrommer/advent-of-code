module Main where

import Prelude as P
import Data.Set as S
import Data.Maybe (mapMaybe)
import Data.Tuple.Lazy (mapFst)
import Control.Arrow ((&&&))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> ([Bool], Set [Bool])
parse = (parseInit &&& parseNotes) . lines

parseInit :: [String] -> [Bool]
parseInit = P.map isPlant . P.drop 15 . head

parseNotes :: [String] -> Set [Bool]
parseNotes = fromList . mapMaybe parseNote . P.drop 2

parseNote :: String -> Maybe [Bool]
parseNote = fmap getPlants . nothingIf getResult
    where
        getResult = isPlant . flip (!!) 9
        getPlants = P.map isPlant . P.take 5

isPlant :: Char -> Bool
isPlant = (==) '#'

part1 :: ([Bool], Set [Bool]) -> Int
part1 input = score $ allGenerations input !! 20

-- Visual inspection shows that the generations' score after the 100th each
-- grow with 62 points.
part2 :: ([Bool], Set [Bool]) -> Int
part2 input = (score $ allGenerations input !! 100) + ((50000000000 - 100) * 62)

allGenerations :: ([Bool], Set [Bool]) -> [(Int, [Bool])]
allGenerations (pots, notes) = iterate (nextGeneration notes) (0, pots)

nextGeneration :: Set [Bool] -> (Int, [Bool]) -> (Int, [Bool])
nextGeneration notes (i, pots) = (i', pots')
    where
        (e, pots') = removeEmptyPots $ P.map (nextPot notes) $ windows 5 $ addEmptyPots pots
        i'         = i - 2 + e

addEmptyPots :: [Bool] -> [Bool]
addEmptyPots pots = emptyPots ++ pots ++ emptyPots
    where
        emptyPots = replicate 4 False

removeEmptyPots :: [Bool] -> (Int, [Bool])
removeEmptyPots = mapFst length . spanLeading . dropTrailing
    where
        dropTrailing = reverse . dropWhile (False ==) . reverse
        spanLeading  = span (False ==)

windows :: Int -> [a] -> [[a]]
windows n xs | length xs < n = []
             | otherwise     = P.take n xs : windows n (tail xs)

nextPot :: Set [Bool] -> [Bool] -> Bool
nextPot notes pots = pots `member` notes

score :: (Int, [Bool]) -> Int
score (i, pots) = sum $ P.map fst $ P.filter snd $ zip [i ..] pots

fromBool :: Bool -> Int
fromBool True  = 1
fromBool False = 0

nothingIf :: (a -> Bool) -> a -> Maybe a
nothingIf p x | p x       = Just x
              | otherwise = Nothing
