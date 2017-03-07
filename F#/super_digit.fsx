let rec superDigit x = 
    if (String.length x) = 1 then (int x)
    else superDigit ((List.fold (fun acc c -> acc + c) 0 [for c in x -> (int c)-48]) |> string) 

let lstx = (System.Console.ReadLine().Split [|' '|])
let n = lstx.[0]
let k = lstx.[1]

printfn "%d" ((superDigit n)*(int k) |> string |> superDigit)