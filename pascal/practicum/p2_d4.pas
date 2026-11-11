{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_d4 (input, output);
var
    N : integer;

function F(N : integer) : integer;
function step(n, i: integer): integer;
begin
    if n mod i = 0 then
        step := step(n div i, i + 1)
    else if n <> 1 then
        step := -1
    else
        step := i - 1
end;

begin
    F := step(n, 2);
end;

begin
    read(N);
    writeln(F(N));
end.
