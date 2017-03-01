let numCases = System.Console.ReadLine() |> int

let arrx = Array.init 1001 (fun i -> Array.init 1001 (fun j -> 0))

for i in 0 .. 1000 do 
    for j in 0 .. i do
        if j = 0 then arrx.[i].[j] <- 1
        elif j = 1 then arrx.[i].[j] <- i
        elif j = i then arrx.[i].[j] <- 1
        else arrx.[i].[j] <- (arrx.[i-1].[j-1] + arrx.[i-1].[j])%100000007
        
for n in 1 .. numCases do 
    let lsty = (System.Console.ReadLine().Split [|' '|])
    let n = lsty.[0] |> int
    let k = lsty.[1] |> int
    printfn "%d" ((arrx.[n].[k])%100000007)