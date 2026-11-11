{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p3_1 (input, output);
const
    n = 5;
type
    vector = array [1..n] of integer;
    matrix = array[1..n] of vector;
var
    A : matrix;

procedure InputMatrix (var A : matrix);
var
    i, j : integer;
begin
    for i := 1 to n do
        for j := 1 to n do
            read(A[i,j])
end;

function IsOrthonormal(var A: matrix): boolean;
var
    i, j, mul : integer;
    f : boolean;
    
    function Skalar(var x, y: vector): integer;
    var
        r, i : integer;
    begin
        r := 0;
        for i := 1 to n do
            r := r + x[i]*y[i];
        Skalar := r
    end;
    
begin
    i := 1;
    j := 1;
    f := True;
    while (i <= n) and f do begin 
        while (j <= n) and f do begin
            mul := Skalar(A[i], A[j]);
            if not((i = j) and (mul = 1) or (i <> j) and (mul = 0)) then
                f := False;
            j := j + 1;
        end;
        i := i + 1;
        j := i;
    end;
    IsOrthonormal := f;
end;

begin
    InputMatrix(A);
    writeln(IsOrthonormal(A));
end.



    
    
