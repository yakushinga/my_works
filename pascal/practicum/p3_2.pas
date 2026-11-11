{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p3_2 (input, output);
type
    integer = int64;
var
    n : integer;
function IsSame(n : integer): boolean;
var
    D : set of 0..9;
    
    function step(n : integer): boolean;
    begin
        if n = 0 then
            step := False
        else if n mod 10 in D then
            step := True
        else begin
            D := D + [n mod 10];
            step := step(n div 10);
        end
    end;

begin
    D := [];
    IsSame := step(n)
end;

begin
    read(n);
    while n <> 0 do begin
        write(n, ':', IsSame(n), ' ');
        read(n)
    end;
    writeln
end.
