open System

let n = Console.ReadLine() |> int

let rec perm listx listy= 
    match listx with
    | [] -> System.String ((List.rev listy) |> List.toArray)
    | x::z -> 
        let temp_list = z.Head::listy
        perm z.Tail (x::temp_list)

for i = 1 to n do
    let line = [for x in Console.ReadLine() -> x]
    printfn "%s" (perm line [])