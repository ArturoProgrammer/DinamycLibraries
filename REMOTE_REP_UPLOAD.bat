@echo off

cd DinamycLibraries
git status

::AGREGA LOS CAMBIOS
echo ACTUALIZANDO REPOSITORIO LOCAL...
git add .
git status

::SE CREA EL COMMIT
set /p commit_comment=¿Cual sera el nombre de este commit? 
git commit -m "%commit_comment%"

::SE SUBE AL REPOSITORIO REMOTO
git push -u origin dev