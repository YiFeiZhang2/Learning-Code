(*
let countColour (lstx, c) = 
    let rec countHelper (lstx, c, acc) = 
        match lstx with
        | [] -> acc
        | x::xs when x = c -> countHelper (xs, c, (acc+1))
        | x::xs when x <> c -> countHelper (xs, c, acc)
    countHelper (lstx, c, 0)

let rec prefixDifference (lstx, a, b) = //takes reversed list
    match lstx with
    | [] -> true
    | x::xs -> 
        if (countColour (lstx, a)) - (countColour (lstx, b)) > 1 then false
        else prefixDifference (xs, a, b)

for i = (System.Console.ReadLine() |> int) downto 1 do
    let s = [for c in System.Console.ReadLine() -> c]
    if (countColour (s, 'R')) <> (countColour (s, 'G')) then printfn "False"
    elif (countColour (s, 'Y')) <> (countColour (s, 'B')) then printfn "False"
    else match (prefixDifference ((List.rev s), 'R', 'G'), prefixDifference ((List.rev s), 'Y', 'B')) with 
            | (true, true) -> printfn "True"
            | (_, _) -> printfn "False"
*) //the above version runs in O(n^2), times out
//below version runs in O(n)

let rec isPerfectColour (lstx, nr, ng, nb, ny) = 
    if (abs (nr-ng)) > 1 then printfn "False"
    elif (abs (nb-ny)) > 1 then printfn "False"
    else match lstx with 
    | [] when (nr = ng) && (nb = ny) -> printfn "True"
    | [] -> printfn "False"
    | x::xs ->
        match x with 
        | 'R' -> isPerfectColour (xs, (nr+1), ng, nb, ny)
        | 'G' -> isPerfectColour (xs, nr, (ng+1), nb, ny)
        | 'B' -> isPerfectColour (xs, nr, ng, (nb+1), ny)
        | 'Y' -> isPerfectColour (xs, nr, ng, nb, (ny+1))
        | _ -> isPerfectColour (xs, nr, ng, nb, ny)

for i = (System.Console.ReadLine() |> int) downto 1 do
    let s = [for c in System.Console.ReadLine() -> c]
    isPerfectColour (s, 0, 0, 0, 0)
