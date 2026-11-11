{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z6_31 (input, output);
var
    n, k, i, m : integer;
begin
    write ('Enter a number: ');
    readln(n);
    for i := 0 to n do begin
        k := 1;
        m := i;
        write ( m, ' = ');
        while m div k >= 3 do
            k := k * 3;
        while k <> 0 do begin
            write (m div k);
            m := m mod k;
            k := k div 3;
        end;
        writeln(' in ternary.')
    end
end.
