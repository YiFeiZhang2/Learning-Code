let n = System.Console.ReadLine() |> float
let x = System.Console.ReadLine() |> float

let numSumsOfPowers n x = 
    let rec sumsHelper n x l = 
        if (n = 0.0) then 1
        else
            if (l = 0.0) then 0
            else
                if l**x > n then sumsHelper n x (l-1.0)
                elif l**x = n then (1 + sumsHelper n x (l-1.0))
                else (sumsHelper (n-(l**x)) x (l-1.0)) + (sumsHelper (n) x (l-1.0))
    sumsHelper n x (ceil (n**(1.0/x)))

printf "%d" (numSumsOfPowers n x)

