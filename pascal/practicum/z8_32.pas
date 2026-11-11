{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program z8_32 (input, output);
const
    n = 5;
type
    vector = array [1..n] of integer;
var
    z : vector;
    ok : vector;
    k : 0..n;
    i, j : integer;

procedure read_array ( var m : vector );
var 
    i : 1..n;
begin
    for i := 1 to n do
        read(m[i])
end;

procedure write_array ( var m : vector );
var 
    i : 1..n;
begin
    for i := 1 to n do
        write(m[i], ' ');
    writeln;
end;

begin
    read_array(z);
    for i := 1 to n do
        ok[i] := 0;
    
    k := 0;
    for i := 1 to n-1 do begin
        for j := i + 1 to n do
            if z[j] > z[i] then
                ok[j] := ok[j] + 1;
    end;
    
    for i := 2 to n do
        if ok[i] = i - 1 then
            k := k + 1;
    writeln(k);
end.
