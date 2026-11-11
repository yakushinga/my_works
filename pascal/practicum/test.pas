{$mode objfpc}
{$codepage UTF8}
program test;
begin
  SetTextCodePage(Output, CP_UTF8);
  writeln('Привет, мир!');
end.
