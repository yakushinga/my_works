{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program p1_3 (input, output);
var
    c1, c2 : char;
begin
    read(c1, c2);
    if c2 = '.' then
        write(c1)
    else begin
        if not((c1 = 'O') and (c2 = 'K')) and (c1 <> 'O') then
            write(c1);
        while c2 <> '.' do begin
            if not((c1 = 'O') and (c2 = 'K')) then begin
                if c1 = 'O' then
                    write(c1);
                if c2 <> 'O' then
                    write(c2);
            end;
            c1 := c2;
            read(c2)
        end;
        if c1 = 'O' then
            write(c1)
    end;
    writeln;
end.
