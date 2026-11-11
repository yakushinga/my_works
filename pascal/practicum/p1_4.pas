{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_4 (input, output);
var
    a, b, k, max : integer;
begin
    max := 0;
    read(b);
    a := 0;
    k := 1;
    repeat
        if a = b then
            k := k + 1
        else begin
            if k > max then
                max := k;
            k := 1
        end;
        a := b;
        read(b)
    until b = 0;
    if k > max then
        max := k;
    writeln(max)
end.
