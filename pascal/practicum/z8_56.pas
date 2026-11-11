{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program z8_31v (input, output);
var
    times : array['a'..'z'] of integer;
    c, i : char;
begin
    for i := 'a' to 'z' do
        times[i] := 0;
    read(c);
    while c <> '.' do begin
        times[c] := times[c] + 1;
        read(c);
    end;
    for i := 'a' to 'z' do
        if times[i] = 1 then
            write(i, ' ');
    writeln
end.
