Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} |
Select-Object TimeCreated, Id, LevelDisplayName, Message |
Format-List
