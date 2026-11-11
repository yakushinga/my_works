{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z7_21 (input, output);
type
    ed = (decimeter, kilometer, meter, millimeter, santimeter);
    length = real;
var
    x : length;
    p : ed;
    
begin
    read(x);
    p := millimeter;
    case p of
        decimeter : x := x / 10;
        kilometer : x := x * 1000;
        meter :;
        millimeter : x := x / 1000;
        santimeter : x := x / 100;
    end;
    write(x:1:5);
end.
