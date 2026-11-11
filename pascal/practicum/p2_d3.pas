{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program p2_d3 (input, output);
type
    matrix = array[1..100, 1..20] of integer;
var
    n, m : integer;
    A : matrix;

procedure sneak(n, m : integer; var A: matrix); 
    procedure insert(dir: char; start, ryad, k, i, j, maxk: integer; var A: matrix; var n, m: integer);
    begin
        A[i, j] := k;
        if k < n*m then
        case dir of
            'r' : begin
                if k < maxk then
                    insert('r', start, ryad, k + 1, i, j + 1, maxk, A, n, m)
                else
                    insert('d', k, ryad, k + 1, i + 1, j, k + n - 2 * ryad - 1, A, n, m)
            end;
            'd' : begin
                if k < maxk then
                    insert('d', start, ryad, k + 1, i + 1, j, maxk, A, n, m)
                else
                    insert('l', k, ryad, k + 1, i, j - 1, k + m - 2 * ryad - 1, A, n, m)
            end;
            'l' : begin
                if k < maxk then
                    insert('l', start, ryad, k + 1, i, j - 1, maxk, A, n, m)
                else
                    insert('u', k, ryad, k + 1, i - 1, j, k + n - 2 * ryad - 2, A, n, m)
            end;
            'u' : begin
                if k < maxk then
                    insert('u', start, ryad, k + 1, i - 1, j, maxk, A, n, m)
                else
                    insert('r', k, ryad + 1, k + 1, i, j + 1, k + m - 2 * ryad - 2, A, n, m)
            end
        end
    end;

begin
    insert('r', 1, 0, 1, 1, 1, m, A, n, m);
end;

procedure print(n, m : integer; var A: matrix);
var 
    i, j, k, l : integer;
begin
    k := 2;
    l := 10;
    while l < m * n do begin
        k := k + 1;
        l := l * 10;
    end;
    for i := 1 to n do begin
        for j := 1 to m do
            write(A[i,j]:k);
        writeln
    end;
end;

begin
    read(n, m);
    sneak(n, m, A);
    print(n, m, A);
end.
