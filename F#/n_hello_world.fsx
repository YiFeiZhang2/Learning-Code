//prints out Hello World n times, where
//n is taken from stdin
open System;;

let num = Console.ReadLine() |> int;;

let rec print_hello n: int = 
    if n = 0 
        then 0
    else 
        printfn "Hello World"
        print_hello (n-1);;

print_hello num;;