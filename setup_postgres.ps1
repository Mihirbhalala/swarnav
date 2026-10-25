# Swarnav Tour & Travels - Quick PostgreSQL Setup Script
param (
    [string]$Password = ""
)

Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " Swarnav PostgreSQL Setup & Data Migration    " -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""

if (-not $Password) {
    $Password = Read-Host "Enter your local PostgreSQL 'postgres' user password"
}

if (-not $Password) {
    Write-Host "Password cannot be empty. Exiting." -ForegroundColor Red
    exit 1
}

$envFile = Join-Path $PSScriptRoot ".env"
$lines = @()
if (Test-Path $envFile) {
    $lines = Get-Content $envFile | Where-Object { 
        $_ -notmatch '^USE_POSTGRES=' -and 
        $_ -notmatch '^DB_NAME=' -and 
        $_ -notmatch '^DB_USER=' -and 
        $_ -notmatch '^DB_PASSWORD=' -and 
        $_ -notmatch '^DB_HOST=' -and 
        $_ -notmatch '^DB_PORT=' 
    }
}

$lines += "USE_POSTGRES=True"
$lines += "DB_NAME=swarnav_db"
$lines += "DB_USER=postgres"
$lines += "DB_PASSWORD=$Password"
$lines += "DB_HOST=localhost"
$lines += "DB_PORT=5432"

Set-Content -Path $envFile -Value $lines -Encoding utf8
Write-Host "[OK] Updated .env with PostgreSQL settings." -ForegroundColor Green
Write-Host ""
Write-Host "Running automated database creation, migrations & data restore..." -ForegroundColor Yellow

& ".\venv\Scripts\python.exe" manage.py load_sqlite_backup

Write-Host ""
Write-Host "All set! You can now start the dev server:" -ForegroundColor Green
Write-Host "  .\venv\Scripts\python.exe manage.py runserver" -ForegroundColor White
