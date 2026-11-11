{$mode TP}
{$R+,B+,X-}
{$codepage UTF-8}
program z9_7 (input, output);
type
    island = (Barbados, Haiti, Grenada, Cuba, Martinika, Yamaika);
    month = (jan, feb, mar, apr, may, jun, jul, aug, sep, okt, nov, dec);
var
    t : array [island, month] of real;
    i, isl : island;
    m, mon : month;
    mint : real;

begin
    mint := t[Barbados, jan];
    for i := Barbados to Yamaika do
        for j := jan to dec do
            if t[i,j] < mint then begin
                mint := t[i, j];
                isl := i;
                mon := j;
            end;
    writeln(isl, mon);
end.
