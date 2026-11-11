{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p4_1 (input, output, fin, fout);
type
    TF = Text;
var
    fin, fout : TF;

procedure Copy(var fin, fout: TF);
var
    s : packed array[1..10] of char;
    i,j : integer;
begin
    reset(fin);
    rewrite(fout);
    while not eof(fin) do begin
        i := 0;
        while (i < 10) and not eoln(fin) do begin
            i := i + 1;
            read(fin, s[i])
        end;
        if eoln(fin) and (i > 0) then begin
            for j := 1 to i do
                write(fout, s[j]);
            writeln(fout)
        end;
        readln(fin);
    end;
    close(fin);
    close(fout);
end;

begin
    assign(fin, 'in.txt');
    assign(fout, 'out.txt');
    Copy(fin, fout);
end.
