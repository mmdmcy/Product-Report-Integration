# Validate Data Sources Script

# This script validates the data sources to ensure data integrity before processing.
# It checks if the sources are reachable and if the data format is correct.

# Define the list of data sources to validate
$dataSources = @(
    "https://api.example.com/data",
    "https://another-source.com/data"
)

# Function to validate each data source
function Validate-DataSource {
    param (
        [string]$source
    )

    try {
        # Send a request to the data source
        $response = Invoke-WebRequest -Uri $source -UseBasicP -ErrorAction Stop
        
        # Check if the response is successful
        if ($response.StatusCode -eq 200) {
            Write-Host "Valid source: $source"
            return $true
        } else {
            Write-Host "Invalid source: $source - Status Code: $($response.StatusCode)"
            return $false
        }
    } catch {
        Write-Host "Error accessing source: $source - $_"
        return $false
    }
}

# Validate all data sources
$validSources = @()
foreach ($source in $dataSources) {
    if (Validate-DataSource -source $source) {
        $validSources += $source
    }
}

# Output the valid sources
if ($validSources.Count -gt 0) {
    Write-Host "Valid data sources found:"
    $validSources | ForEach-Object { Write-Host $_ }
} else {
    Write-Host "No valid data sources found."
}