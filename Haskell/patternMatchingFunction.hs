isSeven :: Integral a => a -> Bool
isSeven 7 = True
isSeven a = False

factorial :: Integral a => a -> a
factorial 1 = 1
factorial x = x * factorial (x-1)

