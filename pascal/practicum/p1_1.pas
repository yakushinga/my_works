{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_1 (input, output);
var
    n, k: integer;
begin
    read(n);
    k := 1;
    while k <= n do
        k := k * 10;
    if n = 0 then
        n := 101
    else
        n := (k + n)*10 + 1;
    writeln(n);
end.
