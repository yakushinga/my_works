{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p4_4PLUS (input, output, t);
var
    t : Text;

procedure FormulaSMmC(var t: Text);
var
    n : boolean;
    i : integer;

function form(var t: Text): boolean;
var
    c : char;
begin
    if eoln(t) then
        form := False
    else begin
        read(t, c);
        if (c in ['0'..'9']) then
            form := True
        else if (c in ['S', 'M', 'm', 'C']) and not eoln(t) then begin
            read(t, c);
            if c <> '(' then
                form := False
            else if form(t) and not eoln(t) then begin
                read(t, c);
                if (c = ',') and not eoln(t) then begin
                    form := form(t);
                    if not eoln(t) then begin
                        read(t, c);
                        if c <> ')' then
                            form := False;
                    end else
                        form := False
                end else
                    form := False
            end else
                form := False
        end else
            form := False
    end
end;

begin
    reset(t);
    i := 1;
    while not eof(t) do begin
        if not eoln(t) then begin
            n := form(t);
            if not(eoln(t)) then
                n := False;
            writeln(i, ' -> ', n);
        end;
        i := i + 1;
        readln(t)
    end;
    close(t)
end;

begin
    assign(t, 'input_p4_4.txt');
    FormulaSMmC(t)
end.
