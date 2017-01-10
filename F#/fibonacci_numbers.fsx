//Find the nth fibonacci number, where n is input from stdin


open System

let num = Console.ReadLine() |> int

let rec doFib n i acc1 acc2 acc3 = 
    if i = n then acc3
    else doFib n (i+1) acc2 acc3 (acc2 + acc3)

let fib n: int = 
    if n <= 1 then 0
    elif n = 2 then 1
    else doFib n 3 0 1 1

printfn "%d" (fib num)