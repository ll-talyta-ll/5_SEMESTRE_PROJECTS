// Início programa B
program B;


	function f(var x : integer; y : integer): integer;

	var
		z : integer;

	begin
	
		x := 1;
		y := 1;
		z := x + y;
		f := z;

	end;
	var
		x, y, z : integer;

	begin
	
		x := 0;
		y := 0;
		z := 0;
		
		writeln(x, y, z);
	
		z := f(x, y);
		writeln(x, y, z);
		
	// Fim programa B
	end.