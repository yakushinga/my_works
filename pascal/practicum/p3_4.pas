{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p3_4 (input, output);
var
    a, b : integer;
function Divide(a, b: integer): integer;
begin
    if (a - b < 0) and (a + b > 0) or (a - b > 0) and (a + b < 0) then
        Divide := 0
    else if (a < 0) and (b < 0) or (a > 0) and (b > 0) then
        Divide := 1 + Divide(a-b, b)
    else if (a < 0) and (b > 0) or (a > 0) and (b < 0) then
        Divide := -1 + Divide(a+b, b)
end;

begin
    read(a, b);
    writeln(Divide(a, b), '=', a div b)
end.
