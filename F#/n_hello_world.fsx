//prints out Hello World n times, where
//n is taken from stdin
open System

let rec print_hello n: int = 
    if n = 0 
        then 0
    else 
        printfn "Hello World"
        print_hello (n-1)

let line = Console.ReadLine()

let mutable num = 0

if ( System.Int32.TryParse( line, &num ) )then 
    print_hello num
else 
    printfn "Wrong input type"
    0
