# Test Data Collection Script for PowerShell

# This script is designed to test the data collection functionalities of the PowerShell scripts in the product report integration project.

# Define a function to test data fetching
function Test-FetchData {
    # Call the fetch_data.ps1 script
    . ..\data_collection\fetch_data.ps1

    # Check if the data was fetched successfully
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Data fetching test passed."
    } else {
        Write-Host "Data fetching test failed."
    }
}

# Define a function to test data source validation
function Test-ValidateSources {
    # Call the validate_sources.ps1 script
    . ..\data_collection\validate_sources.ps1

    # Check if the validation was successful
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Data source validation test passed."
    } else {
        Write-Host "Data source validation test failed."
    }
}

# Run the tests
Test-FetchData
Test-ValidateSources