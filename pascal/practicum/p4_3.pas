{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p4_3 (input, output, f);
type
    TF = file of integer;
var
    f : TF;
    
procedure insert(var f : TF);
var
    a : integer;
begin
    rewrite(f);
    read(a);
    while a <> 0 do begin
        write(f, a);
        read(a)
    end;
    close(f)
end; 

function Greater(var f: TF): boolean;
var
    max, n : integer;
begin
    reset(f);
    read(f, max);
    while not eof(f) do begin
        read(f, n);
        if (n > max) and not eof(f) then
            max := n;
    end;
    Greater := n > max;
end;

begin
    assign(f, 'input.int');
    insert(f);
    writeln(Greater(f));
end.
