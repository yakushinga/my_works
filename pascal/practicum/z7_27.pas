{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z7_27 (input, output);
type
    direction = (N, E, S, W);
    order = (ahead, right, back, left);
var
    D1, D2 : direction;
    O : order;
    n : integer;
begin
    read(n);
    case n of
        1 : D1 := N;
        2 : D1 := E;
        3 : D1 := S;
        4 : D1 := W
    end;
    
    read(n);
    case n of
        1 : O := ahead;
        2 : O := right;
        3 : O := back;
        4 : O := left
    end;
    
end.
