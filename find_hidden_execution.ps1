Get-CimInstance Win32_Process |
Where-Object {$_.CommandLine -match "encodedcommand|bypass|hidden"} |
Select Name, ProcessId, CommandLine
