{Псевдокомментарии и комментарии - не удалять при сдаче программы!}
{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}      
//=====================================================================
(*                        Extra-2  20 очков                           *)
{             Сначала прочитайте документ  Extra-2.pdf                 }
//=====================================================================

program Extra_2(input, output);
type
    name = (Anna,Alex,Petr,Maria,Elena,Egor,Olga,Pavel,Nadya,Ivan,Igor);
    guests = set of name;
    group = array [name] of guests;
var
    G: group;
    friends: guests;
    
// Здесь дать описание функции Everywhere(G, friends)  

    {ваши описания}


// Вывод  содержимого множества (для тестирования программы):
procedure Print(var friends: guests);
var
    i: name;
begin
    for i := Anna to Igor do
        if i in friends then
            case i of
                Anna:  write('Anna ');
                Alex:  write('Alex ');
                Petr:  write('Petr ');
                Maria: write('Maria ');
                Elena: write('Elena ');
                Egor:  write('Egor ');
                Olga:  write('Olga ');
                Pavel: write('Pavel ');
                Nadya: write('Nadya ');
                Ivan:  write('Ivan ');
                Igor:  write('Igor ') 
            end {of case};
    writeln
end;

function Everywhere(var G: group; var friends: guests): boolean;
var
    i : name;
    f : guests;
begin
    f := [Anna..Igor];
    for i := Anna to Igor do
        f := f * (G[i] + [i]);
    if f = [] then
        Everywhere := False
    else begin
        friends := f;
        Everywhere := True;
    end
end;

begin
    {в разделе операторов этой программы - НИЧЕГО НЕ МЕНЯТЬ !!!}
    writeln('=======================');
    writeln('Extra-2');
    writeln('=======================');
    {Заполнение массива тестовыми данными (при сдаче оставить как было)}   
    G[Anna]  := [Alex,Maria,Elena,Olga,Nadya,Ivan,Igor];
    G[Alex]  := [Petr,Maria,Elena,Olga,Pavel,Ivan,Igor];
    G[Petr]  := [Anna,Alex,Maria,Elena,Ivan];
    G[Maria] := [Anna,Petr,Elena,Egor,Olga,Ivan];
    G[Elena] := [Maria,Egor,Olga,Ivan,Igor];
    G[Egor]  := [Alex,Maria,Elena,Pavel,Ivan,Igor];
    G[Olga]  := [Alex,Maria,Elena,Nadya,Ivan];
    G[Pavel] := [Maria,Elena,Egor,Ivan];
    G[Nadya] := [Alex,Petr,Maria,Elena,Ivan,Igor];
    G[Ivan]  := [Alex,Petr,Maria,Elena,Olga,Pavel];
    G[Igor]  := [Anna,Alex,Petr,Maria,Elena,Ivan];
    {Заметим, что Maria, Elena и Ivan побывали в гостях у всех остальных}
    {Вызов вашей функции Everywhere(G, friends):}
    friends := [];
    if Everywhere(G, friends) then begin
        writeln('Yes: ');
        print(friends) {должны быть напечатаны имена: Maria Elena Ivan}
    end else
        writeln('No !')
end.

