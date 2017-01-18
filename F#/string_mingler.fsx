open System

let s1 = [ for c in Console.ReadLine() -> c ]
let s2 = [ for c in Console.ReadLine() -> c ]

let rec stringMingler s1 s2 acc = 
    match s1 with
    | [] -> acc
    | x::y -> stringMingler s2 y (x::acc)

List.iter (fun x -> printf "%c" x ) (List.rev (stringMingler s1 s2 []))