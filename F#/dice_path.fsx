let rec pathSolver (m, n, t, r, f) = 
    max (pathSolver(m-1, n, t, r, f)) (pathSolver(m, n-1, t, r, f))


for i = (System.Console.ReadLine() |> int) downto 1 do
    let L = System.Console.ReadLine().Split ' ' |> Array.map(fun x -> int(x))
    let M = L.[0]
    let N = L.[1]
    let top = 1
    let right = 4
    let front = 2