{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program z8_31v (input, output);
const
    n = 10;
type
    vector = array [1..n] of 1..10000;
var
    s : vector;
    k, i : integer;

procedure read_array ( var m : vector );
var 
    i : 1..n;
begin
    for i := 1 to n do
        read(m[i])
end;

function is_fib ( var n : integer ) : boolean;
var
    f1, f2, f3: integer;
begin
    f1 := 0;
    f2 := 1;
    f3 := 1;
    while f3 < n do begin
        f1 := f2;
        f2 := f3;
        f3 := f1 + f2;
    end;
    is_fib := f3 = n
end;

begin
    read_array(s);
    k := 0;
    for i := 1 to n do
        if is_fib(s[i]) then
            k := k + 1;
    writeln(k);
end.
