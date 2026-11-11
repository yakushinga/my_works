{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program z9_11 (input, output);
type
    matrix = array [1..7, 1..4] of real;
var
    A : matrix;
    maxel, buf : real;
    i, j, p, q : integer;

begin
    for i := 1 to 7 do
        for j := 1 to 4 do
            read(A[i,j]);
    maxel := A[1,1];
    for i := 1 to 7 do
        for j := 1 to 4 do
            if A[i, j] > maxel then begin
                maxel := A[i, j];
                p := i;
                q := j
            end;
    for j := q - 1 downto 1 do
        for i := 1 to 7 do begin
            buf := A[i, j + 1];
            A[i, j+1] := A[i, j];
            A[i, j] := buf
        end;
    for i := p - 1 downto 1 do
        for j := 1 to 4 do begin
            buf := A[i + 1, j];
            A[i + 1, j] := A[i, j];
            A[i, j] := buf
        end;
    for i := 1 to 7 do begin
        for j := 1 to 4 do
            write(A[i, j]:1:1, ' ');
        writeln;
    end
end.
