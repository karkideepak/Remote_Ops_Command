Get-ChildItem "C:\Users" -Recurse -Include *.exe,*.dll,*.ps1 `
-ErrorAction SilentlyContinue |
Where-Object {
    $_.LastWriteTime -gt (Get-Date).AddHours(-12)
} |
Select FullName, LastWriteTime
