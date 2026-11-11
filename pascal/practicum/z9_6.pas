{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program z9_6 (input, output);
const
    n = 3;
type
    point = array [(x, y)] of real;
var
    m : array [1..n] of point;
    d, maxd : real;
    i, j : integer;

begin
    for i := 1 to n do
        read(m[i,x], m[i,y]);
    
    maxd := 0;
    for i := 1 to n - 1 do
        for j := i + 1 to n do begin
            d := sqr(m[i,x] - m[j,x]) + sqr(m[i,y] - m[j,y]);
            if d > maxd then
                maxd := d
        end;
    maxd := sqrt(maxd);
    writeln(maxd:1:4);
end.
