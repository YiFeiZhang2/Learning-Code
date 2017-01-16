//takes n lines from stdin, and puts them into a list of length n
//reverses list

open System

let listx = 
    Seq.initInfinite (fun _ -> Console.ReadLine())
    |> Seq.takeWhile (String.IsNullOrWhiteSpace >> not)
    |> Seq.toList
    
let rec rev listx listy = 
    match listx with
    | [] -> listy
    | x::xs -> rev xs (x::listy)
    
let rev_list = rev listx []

List.iter (fun x -> printfn "%s" x) rev_list