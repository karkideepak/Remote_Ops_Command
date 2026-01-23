# SentinelOne Agent Online Check
# defensive scripting with validation

$serviceName = "Sentinel Agent"

try {
    $service = Get-Service -Name $serviceName -ErrorAction Stop

    if ($service.Status -eq "Running") {
        Write-Output "ONLINE: SentinelOne agent is running."
        exit 0
    } else {
        Write-Output "OFFLINE: SentinelOne agent installed but not running."
        exit 1
    }
}
catch {
    Write-Output "OFFLINE: SentinelOne agent not installed or service missing."
    exit 2
}
