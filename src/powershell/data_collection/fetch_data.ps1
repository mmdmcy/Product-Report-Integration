# PowerShell script to fetch data from various sources for report generation

# Define the data sources
$dataSources = @(
    @{
        Name = "Source1"
        Url = "https://api.source1.com/data"
        Type = "API"
    },
    @{
        Name = "Source2"
        Url = "C:\data\source2.csv"
        Type = "File"
    }
)

# Function to fetch data from API
function Fetch-ApiData {
    param (
        [string]$url
    )
    try {
        $response = Invoke-RestMethod -Uri $url -Method Get
        return $response
    } catch {
        Write-Error "Failed to fetch data from API: $_"
        return $null
    }
}

# Function to fetch data from file
function Fetch-FileData {
    param (
        [string]$filePath
    )
    try {
        $data = Import-Csv -Path $filePath
        return $data
    } catch {
        Write-Error "Failed to fetch data from file: $_"
        return $null
    }
}

# Main data fetching logic
$dataCollection = @()

foreach ($source in $dataSources) {
    if ($source.Type -eq "API") {
        $data = Fetch-ApiData -url $source.Url
        if ($data) {
            $dataCollection += $data
        }
    } elseif ($source.Type -eq "File") {
        $data = Fetch-FileData -filePath $source.Url
        if ($data) {
            $dataCollection += $data
        }
    }
}

# Output the collected data
$dataCollection | ConvertTo-Json | Out-File -FilePath "C:\data\collected_data.json" -Force

Write-Host "Data collection completed. Collected data saved to C:\data\collected_data.json"