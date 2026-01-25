Get-CimInstance Win32_Process |
Where-Object {
    $_.ParentProcessId -in (
        (Get-Process explorer).Id
    )
} |
Select Name, ProcessId, ParentProcessId, CommandLine
