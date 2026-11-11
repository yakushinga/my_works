{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z6_33 (input, output);
var
    n, k : integer;
    c : char;
begin
    write('Enter a number: ');
    read(c);
    n := 0;
    repeat
        n := n * 8 + ord(c) - ord('0');
        read(c)
    until c = ' ';
    k := 1;
    while n div k >= 5 do
        k := k * 5;
    repeat
        write(n div k);
        n := n mod k;
        k := k div 5
    until k = 0;
end.
