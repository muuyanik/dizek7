@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$w=New-Object -ComObject WScript.Shell;$loc=(Get-Location).Path;$s=$w.CreateShortcut((Join-Path $loc 'Dizek 7.lnk'));$s.TargetPath=(Join-Path $loc 'dizek.html');$s.WorkingDirectory=$loc;$s.IconLocation=((Join-Path $loc 'dizek.ico') + ',0');$s.Save()"
echo Kısayol başarıyla güncellendi: Dizek 7.lnk
