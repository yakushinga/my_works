{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p3_d1 (input, output);
const
    n = 5;
type
    matrix = array[1..n, 1..n] of integer;
var
    a : matrix;

procedure InputMatrix (var A : matrix);
var
    i, j : integer;
begin
    for i := 1 to n do
        for j := 1 to n do
            read(A[i,j])
end;

function IsLatinSquare(var A : matrix): boolean;
var
    i, j : integer;
    f : boolean;
    S : set of 0..255;

begin
    i := 1;
    f := True;
    while (i <= n) and f do begin
        S := [1..n];
        j := 1;
        while (j <= n) and f do begin
            if not(A[i,j] in S) then
                f := False
            else
                S := S - [A[i,j]];
            j := j + 1
        end;
        i := i + 1
    end;
    
    i := 1;
    while (i <= n) and f do begin
        S := [1..n];
        j := 1;
        while (j <= n) and f do begin
            if not(A[j, i] in S) then
                f := False
            else
                S := S - [A[j, i]];
            j := j + 1
        end;
        i := i + 1
    end;
    
    IsLatinSquare := f
end;

begin
    InputMatrix(A);
    writeln(IsLatinSquare(A))
end.
