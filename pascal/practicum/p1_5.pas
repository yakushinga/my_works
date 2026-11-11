{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_5 (input, output);
var
    n, i : integer;
begin
    read(n);
    write(n, ' = ');
    i := 2;
    while (i*i <= n) do begin
        if n mod i = 0 then begin
            n := n div i;
            write( i, '*' )
        end else
            i := i + 1
    end;
    write(n)
end.
