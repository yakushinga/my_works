{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z6_32 (input, output);
var
    max, n : integer;
    c : char;
begin
    max := -1;
    repeat
        n := 0;
        read(c);
        repeat
            n := n * 7 + ord(c) - ord('0');
            read(c)
        until (c = ' ') or (c = '.');
        if n > max then
            max := n;
    until c = '.';
    writeln(max)
end.
