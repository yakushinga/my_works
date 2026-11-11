{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z6_23g (input, output);
var
    c1, c2 : char;
begin
    read(c1);
    if c1 <> '.' then begin
        read(c2);
        if c2 <> '.' then
            while c2 <> '.' do begin
                if (c1 = 'p') and (c2 = 'h') then
                    write('f')
                else if (c1 = 'p') then
                    write(c1)
                else if (c2 <> 'p') then
                    write(c2);
                c1 := c2;
                read(c2);
            end
        else
            write(c1);
    end
end.
