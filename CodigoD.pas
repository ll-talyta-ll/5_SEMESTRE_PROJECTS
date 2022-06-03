// Início programa D
program D;
	function f(var x : integer; var y : integer): integer;
	begin
		x := 1;
		y := 1;
		f := x + y;
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
		
	// Fim programa D
	end.