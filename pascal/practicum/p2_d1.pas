{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_d1 (input, output);
type
    integer = int64;
var
    n :integer;

function Delete3 (n : integer) : integer;
var
    c : integer;
begin
    if n < 10 then
        if n = 3 then
            Delete3 := 0
        else
            Delete3 := n
    else begin
        c := n mod 10;
        if c <> 3 then
            Delete3 := c + Delete3(n div 10) * 10
        else
            Delete3 := Delete3(n div 10)
    end;
end;    

begin
    read(n);
    writeln(Delete3(n))
end.
