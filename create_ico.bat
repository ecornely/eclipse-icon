@echo off

setlocal
rem SET te path to the installation of ImageMagic http://www.imagemagick.org/script/binary-releases.php
SET PATH=C:\corne\programs\ImageMagic-6.9.3-2-portable-Q16-x64

for %%p in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    convert -adjoin letter/eclipse_16_%%p.png letter/eclipse_32_%%p.png letter/eclipse_256_%%p.png letter/eclipse_48_%%p.png icos/eclipse_%%p.ico
)
endlocal