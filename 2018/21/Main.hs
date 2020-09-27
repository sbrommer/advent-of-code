module Main where

import Prelude as P
import Data.Char (toUpper)
import Data.List (intercalate, find, nub)
import Data.List.Split (splitOn)
import Data.List.Tools (setAt, dropUntil, takeUntil)
import Data.Maybe (fromJust)
import Data.Bits ((.&.), (.|.))
import Control.Arrow ((&&&))

type Register = [Int]

data Program = Program {ip :: Int, instructions :: [Instruction]}

data Instruction = Instruction { op :: Operation
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
               deriving (Enum, Eq, Ord, Show, Read)

instance Show Program where
    show (Program ip instructions) =
        intercalate "\n" $ show ip : P.map show instructions

instance Show Instruction where
    show (Instruction op a b c) =
        unwords $ show op : P.map show [a, b, c]

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse contents

parse :: String -> Program
parse = parseProgram . lines

parseProgram :: [String] -> Program
parseProgram = uncurry Program . ((parseIp . head) &&& (parseInstructions . tail))

parseIp :: String -> Int
parseIp = read . last . splitOn " "

parseInstructions :: [String] -> [Instruction]
parseInstructions = P.map parseInstruction

parseInstruction :: String -> Instruction
parseInstruction line = Instruction operation a b c
    where
        op:params = splitOn " " line
        [a, b, c] = P.map read params
        operation = read $ P.map toUpper op

run :: Program -> Register -> [Register]
run (Program ip instructions) = run'
    where
        run' :: Register -> [Register]
        run' reg
            | ip' >= length instructions = [reg']
            | otherwise = reg : run' ((reg' `setAt` ip) ip')
            where
                (Instruction op a b c) = instructions !! (reg !! ip)
                reg'   = (reg `setAt` c) result
                ip'    = (reg' !! ip) + 1
                result = runOperation op reg a b

runOperation :: Operation -> Register -> Int -> Int -> Int
runOperation op reg a b =
    case op of
        ADDR -> aValue  +  bValue
        ADDI -> aValue  +  b
        MULR -> aValue  *  bValue
        MULI -> aValue  *  b
        BANR -> aValue .&. bValue
        BANI -> aValue .&. b
        BORR -> aValue .|. bValue
        BORI -> aValue .|. b
        SETR -> aValue
        SETI -> a
        GTIR -> bool2int $ a      >  bValue
        GTRI -> bool2int $ aValue >  b
        GTRR -> bool2int $ aValue >  bValue
        EQIR -> bool2int $ a      == bValue
        EQRI -> bool2int $ aValue == b
        EQRR -> bool2int $ aValue == bValue
    where
        aValue = reg !! a
        bValue = reg !! b

bool2int :: Bool -> Int
bool2int True  = 1
bool2int False = 0

halt :: Program -> [Int]
halt program = P.map (!! 1) $ P.filter instruction30 $ run program [0, 0, 0, 0, 0, 0]
    where
        instruction30 register = register !! 2 == 30

part1 :: Program -> Int
part1 program = head $ halt program

part2 :: Program -> String
part2 program = "See code.py"
