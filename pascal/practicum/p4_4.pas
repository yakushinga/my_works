{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p4_4 (input, output, t);
var
    t : Text;

procedure FormulaSMmC(var t: Text);
var
    n : integer;

function form(var t: Text): integer;
var
    c, c1 : char;
    n, op : integer;
begin
    read(t, c);
    write(c);
    if c in ['0'..'9'] then
        form := ord(c) - ord('0')
    else begin
        c1 := c;
        read(t, c);
        write(c);
        case c1 of
            'M' : begin
                n := -Maxint;
                while c <> ')' do begin
                    op := form(t);
                    if op > n then
                        n := op;
                    read(t, c);
                    write(c);
                end;
            end;
            'm' : begin
                n := Maxint;
                while c <> ')' do begin
                    op := form(t);
                    if op < n then
                        n := op;
                    read(t, c);
                    write(c);
                end;
            end;
            'S' : begin
                n := 0;
                while c <> ')' do begin
                    op := form(t);
                    n := n + op;
                    read(t, c);
                    write(c);
                end;
            end;
            'C' : begin
                n := 0;
                while c <> ')' do begin
                    op := form(t);
                    n := n + 1;
                    read(t, c);
                    write(c);
                end;
            end
        end;
        form := n;
    end;            
end;

begin
    reset(t);
    while not eof(t) do begin
        while not eoln(t) do begin
            n := form(t);
            writeln(' = ', n);
        end;
        readln(t)
    end;
    close(t)
end;

begin
    assign(t, 'input_p4_4.txt');
    FormulaSMmC(t)
end.
