{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program z8_31b (input, output);
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

function is_sqr ( n : integer ) : boolean;
var
    i : integer;
begin
    i := 1;
    while i * i < n do
        i := i + 1;
    is_sqr := i * i = n;
end;

begin
    read_array(s);
    k := 0;
    for i := 1 to n do
        if is_sqr(s[i]) then
            k := k + 1;
    writeln(k);
end.
