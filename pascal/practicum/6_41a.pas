{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z6_41a (input, output);
var
    c : char;
    flag : boolean;
    n : integer;
begin
    read(c);
    n := 0;
    flag := True;
    while flag and (c <> '.') do begin
        if (c >= '0') and (c <= '9') then
            n := (n + ord(c) - ord('0')) mod 9
        else
            flag := False;
        read(c)
    end;
    flag := flag and (n = 0);
    writeln(flag);
end.
