{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p3_d4 (input, output);
var
    n : integer;

procedure tree(n : integer);
procedure f(k : integer);
begin
    if k = 0 then
        write('|')
    else begin
        write('/');
        f(k-1);
        write('\');
    end
end;
procedure row(k, ceil : integer);
begin
    if k > ceil then
        row(1, ceil + 1)
    else if ceil <= n then begin
        write('':9-k);
        f(k);
        writeln;
        row(k+1, ceil);
    end
end;

begin
    writeln('^':10);
    row(1, 1);
    writeln('.........|..........');
end;

begin
    read(n);
    tree(n)
end.
