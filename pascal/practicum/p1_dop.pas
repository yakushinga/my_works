{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_dop (input, output);
var
    n, i, j, k : integer;
begin
    read(n);
    for i := 1 to n do begin
        k := abs(n div 2 + 1 - i);
        for j := 1 to k do
            write(' ');
        k := (n div 2 + 1 - k) * 2 - 1;
        for j := 1 to k do
            write('*');
        writeln();
    end;
end.
