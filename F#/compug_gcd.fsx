//Find gcd of two numbers entered through stdin
//numbers are entered on one line, separated by space

open System

let txt = Console.ReadLine()
let txt_split = txt.Split [|' '|]
let num1 = max (txt_split.[0] |> int) (txt_split.[1] |> int)
let num2 = min (txt_split.[0] |> int) (txt_split.[1] |> int)

let rec gcd num1 num2 = 
    if num2 = 0 then num1
    elif num2 = 1 then 1
    else    let div = num1/num2
            let r = num1 - (num1/num2)*num2
            gcd (max r num2) (min r num2)

printfn "%d" (gcd num1 num2)