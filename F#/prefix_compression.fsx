let lstx = [for c in System.Console.ReadLine() -> c]
let lsty = [for c in System.Console.ReadLine() -> c]

let rec prefixCompression lstx lsty = 
    match lstx with 
    | [] -> []
    | x::xs ->
        match lsty with
        | [] -> []
        | y::ys ->
            if x <> y then []
            else 
                x::(prefixCompression xs ys)

let rec printList lstx n = 
    match lstx with 
    | [] -> printf ""
    | x::xs ->
        if n > 0 then (printList xs (n-1))
        else 
            lstx |> List.iter (fun x -> printf "%c" x)

let pre = (prefixCompression lstx lsty)
let preL = pre.Length

printf "%d " preL
pre |> List.iter (fun x -> printf "%c" x)
printfn ""
printf "%d " (lstx.Length - preL)
printList lstx preL
printfn ""
printf "%d " (lsty.Length - preL)
printList lsty preL
printfn ""