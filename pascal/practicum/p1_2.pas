{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_2 (input, output);
var
    c1, c : char;
    d, i, r : integer;
begin
    r := 0;
    for i := 1 to 3 do begin
        read(c);
        r := r*10 + ord(c) - ord('0');
    end;
    read(c);
    while c <> '=' do begin
        d := 0;
        c1 := c;
        for i := 1 to 3 do begin
            read(c);
            d := d*10 + ord(c) - ord('0');
        end;
        if c1 = '+' then
            r := r + d
        else
            r := r - d;
        read(c);
    end;
    writeln(r);
end.
