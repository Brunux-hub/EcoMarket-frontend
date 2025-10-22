param([string]$todoFile)
# Reemplaza 'pick ' por 'reword ' para reescribir todos los mensajes
(Get-Content -Raw -LiteralPath $todoFile) -replace '^pick\s','reword ' | Set-Content -LiteralPath $todoFile
Write-Host "Sequence todo modified: set all picks to reword"