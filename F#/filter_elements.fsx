let mutable num_cases = System.Console.ReadLine() |> int

while num_cases > 0 do 
    match [for c in System.Console.ReadLine() -> c] with
    | [size; k] -> 
        let line = List.sort [for c in System.Console.ReadLine() -> c]
        printf "hi"
    | _ -> printf "hi"
    num_cases <- num_cases - 1