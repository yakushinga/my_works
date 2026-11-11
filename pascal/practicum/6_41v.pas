{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z6_41v (input, output);
var
    c1, c2 : char;
    k : integer;
begin
    read(c1, c2);
    k := (ord(c1) - ord('0')) mod 3;
    while (c2 >= '0') and (c2 <= '9') do begin
        k := (k + ord(c2) - ord('0')) mod 3;
        c1 := c2;
        read(c2);
    end;
    writeln((c2 = '.') and ((ord(c1) - ord('0')) mod 2 = 0 ) and (k = 0))
end.
