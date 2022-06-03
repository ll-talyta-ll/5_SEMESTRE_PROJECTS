// Início programa A2
program A2;


	function f(x, y: integer): integer;
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
		// Inicializando os ponteiros
		px, py, pz : ^integer;
		// Inicializando os endereços
		ax, ay, az : ^word;
	begin
		x := 0;
		y := 0;
		z := 0;
		
		px := @x;
		py := @y;
		pz := @z;

		ax := addr(px);
		ay := addr(py);
		az := addr(pz);
		
		writeln('Endereços ((l-values)) no RA da main:');
		writeln(ax^, ' ', ay^, ' ', az^);
	
		writeln('Valores ((r-values)) no RA da main:');
		writeln(x, y, z);
		
		z:=f(x, y);
		
		writeln('Valores novos (r-values) no RA da main após chamar f:');
		writeln(x, y, z);
		
	// Fim programa A2
    	end.