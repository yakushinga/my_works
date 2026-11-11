{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p3_3 (input, output);
const
    n = 4;
    m = 5;
type
    matrix = array[1..n, 1..m] of 1..100;
var
    A : matrix;

procedure InputMatrix (var A : matrix);
var
    i, j : integer;
begin
    for i := 1 to n do
        for j := 1 to m do
            read(A[i,j])
end;

function IsCommon (var A: matrix): boolean;
var
    G, H : set of 1..100;
    i, j: integer;
begin
    G := [1..100];
    i := 1;
    while (i <= n) and (G <> []) do begin
        H := [];
        for j := 1 to m do
            H := H + [A[i,j]];
        G := G * H;
        i := i + 1
    end;
    if G = [] then
        IsCommon := False
    else begin
        Iscommon := True;
        for i := 1 to 100 do
            if i in G then
                write(i, ' ');
        writeln
    end
end;

begin
    InputMatrix(A);
    write(IsCommon(A));
end.
