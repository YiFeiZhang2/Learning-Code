//Find length of list
open System

let listx = 
    Seq.initInfinite (fun x -> Console.ReadLine())
    |> Seq.takeWhile ( String.IsNullOrWhiteSpace >> not)
    |> Seq.toList

let length listx = 
    let rec helper listx acc = 
        match listx with
        | [] -> acc
        | x::y -> helper y (acc+1)
    helper listx 0

printfn "%d" (length listx)
