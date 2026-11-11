{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program sorts (input, output);
const
    N = 10;
type
    vector = array [1..N] of integer;
var
    A, B : vector;

{
обмен значениями
}
procedure swap (var a, b : integer);
var
    c : integer;
begin
    c := a;
    a := b;
    b := c
end;

{
чтение вектора
}
procedure read_vector(var A: vector);
var
    i : integer;
begin
    write('Enter ', N, ' numbers: ');
    for i := 1 to N do
        read(A[i])
end;

{
печать вектора
}
procedure write_vector(var A: vector);
var
    i : integer;
begin
    for i := 1 to N do
        write(A[i], ' ');
    writeln
end;

{
---сортировка пузырьком---

основная идея - многократный проход по массиву
и смена местами элементов, образующих инверсию

}
procedure bubble_sort(var A: vector);
var
    i, j : integer;
begin
    for i := N downto 2 do
        for j := 1 to i - 1 do
            if A[j] > A[j+1] then 
                swap(A[j], A[j+1])
end;

{
вспомогательная функция для insert_sort
}
function f(var A : vector; i, key : integer): boolean;
begin
    if i > 0 then
        f := A[i] > key
    else
        f := False
end;

{
---сортировка вставками---

основная идея - i-ый элемент встает на нужное место
в отсортированной части массива (с 1 по i-1 элемент)

}
procedure insert_sort(var A: vector);
var
    i, j, key : integer;
begin
    for i := 2 to N do begin
        key := A[i];
        j := i - 1;
        while (j > 0) and f(A, j, key) {вместо (A[j] > key) во free pascal, т.к. там имеются ленивые вычисления} do begin
            A[j+1] := A[j];
            j := j - 1
        end;
        A[j+1] := key;
    end
end;

{
---сортировка выбором---

основная идея - ищем в первых i неотсортированных элементах вектора максимальный
и вставляем его на i-ое место

}
procedure select_sort(var A : vector);
var
    i, j, max : integer;
begin
    for i := N downto 2 do begin
        max := 1;
        for j := 2 to i do
            if (A[j] > A[max]) then
                max := j;
        swap(A[max], A[i]);
    end
end;

{
--разбиение вектора--

вектор разбивается относительно A[r]:
те элементы, меньше или равные ему, становятся левее него
а те, кто больше - становятся правее его

}
procedure partition(var A : vector; l, r : integer; var q : integer);
var
    i, j, x: integer;
begin
    x := A[r];
    i := l - 1; {индекс i - предполагаемое новое место A[r]}
    for j := l to r - 1 do
        if A[j] <= x then begin {нашли элемент меньший или равный A[r] - вставляем его левее предполагаемого нового места A[r]}
            i := i + 1;
            swap(A[i], A[j]);
            write_vector(A);
        end;
    swap(A[i+1], A[r]); {вставляем A[r] на новое место, при этом понимаем, что A[i+1] точно больше A[r]}
    q := i + 1; {индекс нового места A[r]}
    write_vector(A);
end;

{
---быстрая сортировка Хоара---

основная идея - разбиваем вектора на две части относительно A[r], затем
повторяем то же самое для левой и правой части вектора
и так до тех пор, пока в очередном разбиении не останется по одному элементу слева и справа очередного A[r]
}
procedure qsort(var A : vector; l, r : integer);
var
    q : integer;
begin
    if l < r then begin
        partition(A, l, r, q); {элемент A[r] оказался на позиции q - это и есть его законное место, так как все
        правее него - больше него, а все левее - меньше или равны ему, чего мы и хотим добиться для всех элементов в
        результате всего процесса сортировки}
        qsort(A, l, q-1);
        qsort(A, q+1, r);
    end
end;

begin
    read_vector(A);
    B := A;
    bubble_sort(B);
    write ('Bubble sort: ');
    write_vector(B);
    B := A;
    write ('Insert sort: ');
    insert_sort(B);
    write_vector(B);
    B := A;
    write ('Select sort: ');
    select_sort(B);
    write_vector(B);
    B := A;
    write ('Hoar`s quick sort: ');
    qsort(B, 1, N);
    write_vector(B);
end.
