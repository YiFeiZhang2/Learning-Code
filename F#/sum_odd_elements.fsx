//Sum all odd elements of a list

open System

(*USER CODE BEGIN*)
let f arr =
    let rec helper arr acc= 
        match arr with
        | [] -> acc
        | x::y ->
            if x%2 = 1 then helper y (acc+x)
            elif x%2 = -1 then helper y (acc+x)
            else helper y acc
    helper arr 0
(*USER CODE END*)

let read_and_parse()=
    let mutable arr = []
    let mutable buff = Console.ReadLine()
    while buff <> null do
            arr <- Int32.Parse(buff)::arr
            buff <- Console.ReadLine()
    arr

let main =    
    let arr = read_and_parse()
    printf "%A" <| f arr