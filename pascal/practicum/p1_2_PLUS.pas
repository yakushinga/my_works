{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_2_PLUS (input, output);
var
    c1, c : char;
    d, r : integer;
begin
    c1 := '+';
    r := 0;
    while c1 <> '=' do begin
        c := '0';
        d := 0;
        repeat
            d := d * 10 + ord(c) - ord('0');
            read(c);
        until (c < '0') or (c > '9');
        if c1 = '+' then
            r := r + d
        else
            r := r - d;
        c1 := c;
    end;
    writeln(r)
end.
