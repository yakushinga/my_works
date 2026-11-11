{$mode ISO}
{$R+,B+,X-}
{$codepage UTF-8}
program s1_1 (input, output);
type
    TE = integer;
    TF = file of TE;
var
    f1, f2 : TF;
    
procedure CreateFile(var f : TF; n : char);
begin
    write(n, ' = ');
    rewrite(f);
    read(f^);
    while f^ <> 0 do begin
        put(f);
        read(f^)
    end;
    close(f)
end;


procedure PrintFile(var f: TF; n: char);
begin
    write(n, ' : ');
    reset(f);
    while not eof(f) do begin
        write(f^: 4);
        get(f)
    end;
    writeln;
    writeln('-----------------------------------------------------');
    close(f)
end;

function IsEqual(var f1, f2 : TF): boolean;
var
    ok : boolean;
begin
    reset(f1);
    reset(f2);
    ok := true;
    while ok and not eof(f1) and not eof(f2) do begin
        if f1^ = f2^ then begin
            get(f1);
            get(f2)
        end else
            ok := false
    end;
    IsEqual := ok and eof(f1) and eof(f2);
    close(f1);
    close(f2)
end;

begin
    assign(f1, 'f1.int');
    assign(f2, 'f2.int');
    
    CreateFile(f1, '1');
    CreateFile(f2, '1');
    PrintFile(f1, '1');
    PrintFile(f2, '2');
    
    writeln;
    
    writeln(IsEqual(f1, f2))
end.
