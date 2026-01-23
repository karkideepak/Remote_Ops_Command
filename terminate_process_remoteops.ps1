#RemoteOps
$processName = "malware"

$process = Get-Process -Name $processName -ErrorAction SilentlyContinue

if ($process) {
    Stop-Process -InputObject $process -Force
    Write-Output "Process '$processName' terminated successfully."
} else {
    Write-Output "Process '$processName' not found. No action taken."
}
