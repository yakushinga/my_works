{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_d2 (input, output);
var
    n : integer;

function IsPrime(n : integer): boolean;
var
    i : integer;

    function f(var n : integer; i : integer): boolean;
    begin
        if i * i > n then
            f := True
        else if n mod i <> 0 then
            f := f(n, i + 1)
        else
            f := False
    end;

begin
    i := 2;
    IsPrime := f(n, i);
end;

begin
    read(n);
    writeln(IsPrime(n))
end.
