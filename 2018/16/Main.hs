module Main where

import Prelude as P
import Data.IntMap as M
import Data.Set as S
import Data.List.Split (chunksOf, splitOn)
import Data.List.Tools (setAt)
import Data.Tuple.Lazy (mapPair, mapSnd)
import Data.Bits ((.&.), (.|.))
import Control.Arrow ((&&&))

data Sample = Sample { before      :: Register
                     , instruction :: Instruction Int
                     , after       :: Register
                     }

type Register = [Int]

data Instruction a = Instruction { op :: a
                                 , a  :: Int
                                 , b  :: Int
                                 , c  :: Int
                                 }

data Operation = ADDR | ADDI
               | MULR | MULI
               | BANR | BANI
               | BORR | BORI
               | SETR | SETI
               | GTIR | GTRI | GTRR
               | EQIR | EQRI | EQRR
               deriving (Enum, Eq, Ord, Show)

instance Show Sample where
    show (Sample before instruction after) =
        "\nBefore: "   ++ show before      ++
        "\n"           ++ show instruction ++
        "\nAfter:  "   ++ show after       ++
        "\n"

instance Show a => Show (Instruction a) where
    show (Instruction op a b c) =
        show op ++ " " ++
        show a  ++ " " ++
        show b  ++ " " ++
        show c

instance Functor Instruction where
    fmap f instruction = instruction {op = f (op instruction)}

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> ([Sample], [Instruction Int])
parse = mapPair (parseSamples, parseProgram) . P.splitAt 3044 . lines

parseSamples :: [String] -> [Sample]
parseSamples = P.map parseSample . chunksOf 4

parseSample :: [String] -> Sample
parseSample (before : instruction : after : _) =
    Sample (parseRegister    before)
           (parseInstruction instruction)
           (parseRegister    after)

parseRegister :: String -> Register
parseRegister = P.map read . splitOn ", " . init . P.drop 9

parseInstruction :: String -> Instruction Int
parseInstruction line =
    let [op, a, b, c] = P.map read $ splitOn " " line
    in  Instruction op a b c

parseProgram :: [String] -> [Instruction Int]
parseProgram = P.map parseInstruction . dropWhile P.null

run :: Register -> Instruction Operation -> Register
run register (Instruction operation a b c) = (register `setAt` c) result
    where
        result = case operation of
                      ADDR -> register !! a  +  register !! b
                      ADDI -> register !! a  +  b
                      MULR -> register !! a  *  register !! b
                      MULI -> register !! a  *  b
                      BANR -> register !! a .&. register !! b
                      BANI -> register !! a .&. b
                      BORR -> register !! a .|. register !! b
                      BORI -> register !! a .|. b
                      SETR -> register !! a
                      SETI -> a
                      GTIR -> if a             >  register !! b then 1 else 0
                      GTRI -> if register !! a >  b             then 1 else 0
                      GTRR -> if register !! a >  register !! b then 1 else 0
                      EQIR -> if a             == register !! b then 1 else 0
                      EQRI -> if register !! a == b             then 1 else 0
                      EQRR -> if register !! a == register !! b then 1 else 0

part1 :: ([Sample], a) -> Int
part1 = count ((<=) 3 . length . possibleOperations) . fst

possibleOperations :: Sample -> Set Operation
possibleOperations (Sample before instruction after) =
    S.filter (\operation -> run before instruction {op = operation} == after) $ S.fromList [ADDR ..]

count :: (a -> Bool) -> [a] -> Int
count p = length . P.filter p

part2 :: ([Sample], [Instruction Key]) -> Int
part2 (samples, instructions) = head $ P.foldl run register instructions'
    where
        register      = [0, 0, 0, 0]
        operationsMap = nrToOps samples
        instructions' = P.map (fmap (operationsMap !)) instructions

nrToOps :: [Sample] -> IntMap Operation
nrToOps samples = operations
    where
        possibleOps = fromListWith S.intersection $ P.map (op . instruction &&& possibleOperations) samples
        operations  = deriveOps possibleOps

deriveOps :: IntMap (Set Operation) -> IntMap Operation
deriveOps = deriveOps' M.empty

deriveOps' :: IntMap Operation -> IntMap (Set Operation) -> IntMap Operation
deriveOps' ops possibleOps
    | M.null possibleOps = ops
    | otherwise          = deriveOps' ops' possibleOps'
    where
        certainOps   = M.filter ((==) 1 . S.size) possibleOps
        (i, op)      = mapSnd pickFirstS $ pickFirstM certainOps
        ops'         = M.insert i op ops
        possibleOps' = M.map (S.delete op) $ i `M.delete` possibleOps

pickFirstM :: IntMap a -> (Key, a)
pickFirstM = head . M.toList

pickFirstS :: Set a -> a
pickFirstS = head . S.toList
