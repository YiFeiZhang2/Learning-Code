open System

let num_lines = Console.ReadLine() |> int

let fac m =
    let rec helper m n = 
        if m = 0 then 1
        elif m = 1 then n
        else helper (m-1) m*n
    helper m 1

let pascLine m =
    let rec helper m n = 
        if n = m+1 then printfn ""
        else 
            printf "%d " (fac m / (fac n * fac (m-n)))
            helper m (n+1)
    helper m 0

let pasc m = 
    let rec helper m n = 
        if n = m then ()
        else
            pascLine n
            helper m (n+1)
    helper m 0
    
