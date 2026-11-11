{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p4_2 (input, output, fin, fout);
type
    setchar = set of char;
const
    gl = ['e', 'y', 'u', 'i', 'o', 'a'];
var
    fin, fout: Text;
    r, s : setchar;
    c : char;

procedure print_set(var fout: Text; s: setchar);
var
    c : char;
begin
    for c in ['a'..'z'] do
        if c in s then
            write(fout, c);
    writeln(fout)
end;

begin
    r := gl;
    assign(fin, 'words.txt');
    assign(fout, 'test.txt');
    reset(fin);
    rewrite(fout);
    while not eof(fin) do begin
        s := [];
        while not eoln(fin) do begin
            read(fin, c);
            write(fout, c);
            if c in gl then
                s := [c] + s;
        end;
        r := r * s;
        write(fout, ' = ');
        print_set(fout, s);
        readln(fin)
    end;
    print_set(output, gl - r);
    close(fin);
    close(fout);
end.
