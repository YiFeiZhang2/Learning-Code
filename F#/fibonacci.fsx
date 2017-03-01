//Enter your code here. Read input from STDIN. Print output to STDOUT
let mutable n = System.Console.ReadLine() |> int

let fib n = 
    let n0 = 0
    let n1 = 1
    let rec fibHelper s0 s1 n = 
        match n with 
        | 0 -> s0
        | 1 -> s1
        | _ -> fibHelper s1 ((s0+s1)%100000007) (n-1)
    printfn "%d" (fibHelper n0 n1 n)

while n > 0 do 
    let T = System.Console.ReadLine() |> int
    fib T
    n <- n-1
    