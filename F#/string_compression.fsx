open System

let lstx = [for c in Console.ReadLine() -> c]

let sCompress lstz = 
    let rec compressHelper lstx outList = 
        match lstx with 
        | [] -> outList
        | x::xs -> 
            match outList with 
            | [] -> compressHelper xs [(0, x)]
            | o::os -> 
                if (x = (snd o)) then compressHelper xs ((((fst o)+1), x)::os)
                else compressHelper xs ((0, x)::outList)
    let rec printList lstx = 
        match lstx with 
        | [] -> printfn ""
        | (0, c)::cs -> 
            printf "%c" c
            printList cs
        | (i, c)::cs -> 
            printf "%c%d" c (i+1)
            printList cs
    printList (compressHelper lstz [] |> List.rev)
