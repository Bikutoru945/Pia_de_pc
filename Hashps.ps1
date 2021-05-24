$ruta = read-host "ingrese la ruta de los archivos de configuracion"

Get-ChildItem $ruta | Get-FileHash -Algorithm SHA512 | Out-File -FilePath .\Valor_hash.txt