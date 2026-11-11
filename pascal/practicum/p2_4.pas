{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_4 (input, output);
const
    n = 5;
    m = 4;
type
    matrix = array[1..n, 1..m] of real;
var
    A : matrix;
    max : real;
    
procedure read_matrix (var A : matrix);
var
    i, j : integer;
begin
    for i := 1 to n do
        for j := 1 to m do
            read(A[i,j])
end;

procedure MaxMin (var A: matrix; n,m : integer; var max : real);
var
    i, j : integer;
    StrMin : real;
    f : boolean;
begin
    f := True;
    for i := 1 to n do begin
        StrMin := A[i,1];
        for j := 2 to m do
            if A[i,j] < StrMin then
                StrMin := A[i,j];
        
        if (StrMin > max) or f then
            max := StrMin;
        f := False;
    end;

begin
    read_matrix(A);
    MaxMin(A, n, m, max);
    writeln(max:1:6)
end.
