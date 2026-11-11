{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_1 (input, output);
var
    high : array['A'..'Z'] of 0..Maxint;
    low : array['a'..'z'] of 0..Maxint;
    c : char;
begin
    for c := 'A' to 'Z' do
        high[c] := 0;
    for c := 'a' to 'z' do
        low[c] := 0;
    read(c);
    while c <> '.' do begin
        if (c >= 'a') and (c <= 'z') then
            low[c] := low[c] + 1
        else if (c >= 'A') and (c <= 'Z') then
            high[c] := high[c] + 1;
        read(c);
    end;
    for c := 'a' to 'z' do
        if (low[c] > 0) and (low[c] = high[chr(ord(c)-ord('a')+ord('A'))]) then
            write(c);
end.

