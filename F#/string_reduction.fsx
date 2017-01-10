//given a string consisting of lowercase English characters (a-z)
//remove all characters that have previously occurred in the string

open System

let txt = Console.ReadLine()

let rec reducString txt seen = 
    match txt with
    | [] -> List.rev seen
    | x :: y -> if Seq.exists (fun elem -> elem = x) seen then reducString y seen
                else reducString y (x :: seen)

reducString (List.ofSeq txt) [] |> List.toArray |> System.String |> printfn "%s"