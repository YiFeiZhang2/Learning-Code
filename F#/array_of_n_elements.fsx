//Takes an integer from stdin, creates a list of size n filled with 1

open System

let f n = 
    let rec helper n listy= 
        if n = 0 then listy
        else helper (n-1) (1::listy)
    helper n []

let main() =
    let input = Console.ReadLine()
    let n = int input
    printfn "%A" (f n)

main()