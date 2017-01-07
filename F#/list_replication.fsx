//takes a list and repeat each element in list n amount of times
//first input is integer n
//next X lines contain integers which are the elements of the array

open System

let rec printNTimes a n =
    if ( n = 0 ) then printf ""
    else 
        printfn "%s" a
        printNTimes a (n-1)

let rec listReplication listx numReplicate = 
    match listx with
    | [] -> printfn ""
    | x :: listy -> printNTimes x numReplicate
                    listReplication listy numReplicate

let num = Console.ReadLine() |> int

let listx = 
    Seq.initInfinite (fun _ -> Console.ReadLine())
    |> Seq.takeWhile (String.IsNullOrWhiteSpace >> not)
    |> Seq.toList

listReplication listx num
