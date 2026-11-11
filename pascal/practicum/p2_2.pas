{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_2 (input, output);
type
    int = int64;
var
    n, i : int;

procedure Ins3 (var n, i : int);
begin
    if i * 10 > n then
        n := (n div i)*i*10 + 3 * i + n mod i
    else begin
        i := i * 10;
        Ins3(n, i)
    end
end;

begin
    read(n);
    i := 1;
    Ins3(n, i);
    writeln(n);
end.
