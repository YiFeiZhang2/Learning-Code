let lsty = (System.Console.ReadLine().Split [|' '|]).[0]
let n = lsty.[0] |> int
let lstx = List.sort [for c in System.Console.ReadLine() -> (c |> int)] |> List.rev

let rec rFac n lstx acc = 
    match lstx with 
    | [] when (n <> 0) -> [-1]
    | [] when (n = 0) -> acc
    | x::xs -> 
        match (n%x) with 
        | 0 -> rFac (n/x) lstx (x::acc)
        | _ -> rFac n xs acc
        
let rec printLexi facList acc = 
    match facList with 
    | [] -> printf ""
    | x::xs -> 
        printf "%d" (acc*x)
        printLexi xs (acc*x)
        
printf "%A" (rFac n lstx [])
printLexi (rFac n lstx []) 1