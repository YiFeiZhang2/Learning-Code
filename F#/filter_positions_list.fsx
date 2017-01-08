//For a given list with N integers, return new list removing elements at odd positions.
//Input from stdin, N integers each on a separate line

open System

let listx = 
    Seq.initInfinite (fun _ -> Console.ReadLine())
    |> Seq.takeWhile (String.IsNullOrWhiteSpace >> not)
    |> Seq.toList

let splitList listx = List.fold (fun (ind,listy) x -> if ind%2=1 then 
                                                                (ind + 1, x :: listy)
                                                            else (ind + 1, listy) ) (0, []) listx

let filtered_list = snd (splitList listx) |> List.rev

List.iter (fun x -> printfn "%s" x) filtered_list