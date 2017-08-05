// creates all possible board configurations and saves in config.txt
open System.IO
let CIRCLE = 1
let CROSS = 2
let outFile = new StreamWriter("./config.txt")


let rec generate n arr = 
    match n with
    | 0 -> arr
    | _ -> generate (n-1) ((List.map (fun s -> 0::s) arr) @ (List.map (fun s -> 1::s) arr) @ (List.map (fun s -> 2::s) arr))

let states = generate 9 [[]]

List.iter (fun s -> (List.iter (fun x -> outFile.Write(x:int)) s); outFile.WriteLine()) states
outFile.Close()