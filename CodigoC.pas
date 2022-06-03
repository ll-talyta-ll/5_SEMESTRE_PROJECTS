// Início programa C
program C;
	var 
	y : integer;
	function f(var x : integer): integer;

	begin
	
		x := 1;
		f := x + y;
	end;
	
	var
		x, z : integer;
	begin
		x := 0;
		y := 4;
		z := 0;
		writeln(x, y, z);
		z := f(x);
		writeln(x, y, z);
		
	// Fim programa C
	end.