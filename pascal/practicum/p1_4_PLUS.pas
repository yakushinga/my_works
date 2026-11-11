{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_4_PLUS (input, output);
var
    a, b, k, max, i, maxi : integer;
begin
    max := 0;
    read(b);
    a := 0;
    k := 1;
    i := 0;
    repeat
        if a = b then
            k := k + 1
        else begin
            if k > max then begin
                max := k;
                maxi := i
            end;
            i := i + k;
            k := 1
        end;
        a := b;
        read(b);
    until b = 0;
    if k > max then begin
        max := k;
        maxi := i;
    end;
    writeln('pos=', maxi, ' len=', max)
end.
