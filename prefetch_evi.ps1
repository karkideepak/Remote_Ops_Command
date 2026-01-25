Get-ChildItem "C:\Windows\Prefetch" |
Where-Object {
    $_.Name -match "POWERSHELL|CMD|MSHTA|RUNDLL32"
} |
Sort-Object LastWriteTime -Descending |
Select Name, LastWriteTime
