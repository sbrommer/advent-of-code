module Main where

import Prelude as P hiding ((<$>), (<*>), (<*))

import Text.Parsec hiding (count)
import Text.Parsec.String (Parser)

import Data.Map as M
import Data.Set as S
import Data.Char (isAlpha, isDigit)
import Data.Either.Utils (fromRight)
import Data.Tuple.Lazy (mapSnd)

import Control.Arrow ((&&&))
import Control.Applicative hiding ((<|>), many, optional)

type Bag = String
type Rules = Map Bag (Set (Int, Bag))

main :: IO()
main = do
    contents <- readFile "input.txt"
    print $ (part1 &&& part2) $ parse' contents

-- Solutions
part1 :: Rules -> Int
part1 = S.size . descendants "shinygold" . invert . M.map (S.map snd)

invert :: Map Bag (Set Bag) -> Map Bag (Set Bag)
invert graph = M.fromListWith S.union inverse
    where
        inverse = [(v, S.singleton k) | (k, vs) <- M.toList graph, v <- S.toList vs]

descendants :: Bag -> Map Bag (Set Bag) -> Set Bag
descendants bag graph =
    case bag `M.lookup` graph of
         Nothing   -> S.empty
         Just bags -> S.unions $ bags : S.toList (S.map (`descendants` graph) bags)

part2 :: Rules -> Int
part2 = flip count "shinygold"

count :: Rules -> Bag -> Int
count rules = go
    where
        go :: Bag -> Int
        go = sum . P.map (uncurry (*) . mapSnd ((+1) . go)) . S.toList . (!) rules

-- Parse
parse' :: String -> Rules
parse' = fromRight . parse pRules ""

pRules :: Parser Rules
pRules =  M.unions <$> endBy pRule (char '\n')

pRule :: Parser Rules
pRule =  M.singleton <$> pBag <*  string " contain " <*> (pNoBags <|> pSomeBags) <*  char '.'

pBag :: Parser Bag
pBag = (++) <$> (many (satisfy isAlpha) <* char ' ') <*>  many (satisfy isAlpha)
            <*  string " bag" <* optional (string "s")

pNoBags :: Parser (Set (Int, Bag))
pNoBags = S.empty <$ string "no other bags"

pSomeBags :: Parser (Set (Int, Bag))
pSomeBags = S.fromList <$> sepBy pSomeBag (string ", ")

pSomeBag :: Parser (Int, Bag)
pSomeBag = (,) <$> pCount <* char ' ' <*> pBag

pCount :: Parser Int
pCount = read <$> many1 (satisfy isDigit)
