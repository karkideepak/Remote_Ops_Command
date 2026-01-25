Get-CimInstance Win32_Process |
Where-Object {
    $_.CommandLine -match "encodedcommand|frombase64|iex|downloadstring|http"
} |
Select Name, ProcessId, CommandLine
