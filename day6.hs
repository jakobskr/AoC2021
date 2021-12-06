import Data.List
import System.Environment   
import Data.Char

heads (x:xs) = 
    take 6 xs ++ xs!!6 + x : [] ++ drop 7 xs ++ x : []

main = do
    content <- readFile "day6_input"
    let li = map digitToInt (filter (/=',') content)
    let fish2 = map helper [0..8] where
        helper x = (length (filter (==x) (map digitToInt (filter (/=',') content))))
    print fish2
    let it = iterate heads fish2
    print $ sum $ it!!80
    print $ sum $ it!!256