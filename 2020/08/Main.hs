module Main where

import Prelude as P hiding ((<$>), (<*>), (<*), (*>))

import Text.Parsec
import Text.Parsec.String (Parser)

import Data.IntMap as M hiding (mapMaybe)
import Data.Set as S
import Data.Char (isDigit)
import Data.Either.Utils (fromLeft, fromRight)
import Data.Either (rights)
import Data.Maybe (mapMaybe)

import Control.Arrow ((&&&))
import Control.Applicative hiding ((<|>))

data Op = Acc | Jmp | Nop deriving Eq

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse' contents

-- Solution
part1 :: IntMap (Op, Int) -> Int
part1 = fromLeft . run . M.map op

part2 :: IntMap (Op, Int) -> Int
part2 = head . rights . P.map (run . M.map op) . codes

-- Translate instructions to the difference they make in the state.
op :: (Op, Int) -> (Int, Int)
op (Acc, n) = (n, 1)
op (Jmp, n) = (0, n)
op (Nop, _) = (0, 1)

run :: IntMap (Int, Int) -> Either Int Int
run code = go S.empty (0, 0)
    where
        go :: Set Int -> (Int, Int) -> Either Int Int
        go is s@(a, i)
            | i `S.member` is  = Left  a -- The code loops.
            | i >= length code = Right a -- The code terminates.
            | otherwise        = go (i `S.insert` is) $ addTups s $ code ! i -- Recurse; next instruction.

codes :: IntMap (Op, Int) -> [IntMap (Op, Int)]
codes code = mapMaybe swap [0 .. length code - 1]
    where
        swap :: Int -> Maybe (IntMap (Op, Int))
        swap i = case code ! i of
                      (Acc, n) -> Nothing
                      (Jmp, n) -> Just $ M.insert i (Nop, n) code
                      (Nop, n) -> Just $ M.insert i (Jmp, n) code

addTups :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTups (x1, x2) (y1, y2) = (x1 + y1, x2 + y2)

-- Parser
parse' :: String -> IntMap (Op, Int)
parse' = fromRight . parse pCode ""

pCode :: Parser (IntMap (Op, Int))
pCode = M.fromList . zip [0 ..] <$> endBy pInstr (char '\n')

pInstr :: Parser (Op, Int)
pInstr = (,) <$> pOp <* char ' ' <*> pArg

pOp :: Parser Op
pOp =  (Acc <$ string "acc")
   <|> (Jmp <$ string "jmp")
   <|> (Nop <$ string "nop")

pArg :: Parser Int
pArg = (pNeg <|> pPos) <*> pNat
    where
        pNeg = negate <$ char '-'
        pPos = id     <$ char '+'
        pNat = read   <$> many1 (satisfy isDigit)
