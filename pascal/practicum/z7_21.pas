{$mode TP}
{$R+,B+,X-,I+,GOTO-}
{$codepage UTF-8}
program z7_21 (input, output);
type
    country = (Germany, Kuba, Laos, Monako, Nepal, Poland);
    continent = (Asia, America, Europe);
var
    s : country;
    c : continent;
begin
    s := Laos;
    c := Europe;
    case s of
        Germany, Monako, Poland : c := Europe;
        Kuba : c := America;
        Laos, Nepal : c := Asia
    end;
end.
