Display restoreAfter: [ Display fillWhite.
x:= 0.
myPen := Pen new. 
myPen down. 
myPen north. 
myPen color: (Color red).
1 to: 15 do: [:a |
	1 to: 4 do: [:b |myPen go: x; turn: 90.].
	myPen up.
		1 to: 2 do: [:c |myPen go: 10; turn: 90.].
		myPen down.
		myPen north.
		x := x - 20.].]