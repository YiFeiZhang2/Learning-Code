//Filter an array of integers and output values that are
//less than a specified value X. Input taken from stdin
//The first line contains X.
//The next B lines each contain one integer, which 
//represents the elements in the array in order

open System

let num = Console.ReadLine() |> int

let listx = 
    Seq.initInfinite ( fun _ -> Console.ReadLine())
    |> Seq.takeWhile ( String.IsNullOrWhiteSpace >> not )
    |> Seq.map System.Int32.Parse
    |> Seq.toList

let rec filterList (listx: list<int>) num (listy: list<int>)= 
    match listx with
    | [] -> List.rev listy |> List.iter (fun x -> printfn "%d" x)
    | x :: listz -> let nlisty: list<int> = x :: listy
                    if ( x < num ) then filterList listz num nlisty
                    else filterList listz num listy

filterList listx num []