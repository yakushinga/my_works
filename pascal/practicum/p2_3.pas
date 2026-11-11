{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_3 (input, output);
const
    n = 5;
    m = 4;
type
    matrix = array[1..n, 1..m] of integer;
var
    A : matrix;

procedure read_matrix (var A : matrix);
var
    i, j : integer;
begin
    for i := 1 to n do
        for j := 1 to m do
            read(A[i,j])
end;

function is_zero(var A: matrix; i, j : integer) : boolean;
begin
    if i  > n then
        is_zero := True
    else if A[i,j] <> 0 then
        is_zero := False
    else
        is_zero := is_zero(A, i + ord(j mod m = 0), j mod m + 1)
end;

begin
    read_matrix(A);
    write(is_zero(A, 1, 1))
end.
