## 0.2.15 - 2019-03-21
- Fix Job View in 'ADL: Show Jobs' old API depricate.
- Move 'AZURE DATALAKE' Explorer to Azure Container.

## 0.2.14 - 2018-05-22
- Add Extract Builder Functionality for TXT, CSV and TSV files -  
    Add 'Create Extract Script' menu item for ADL files in 'AZURE DATALAKE' Explorer.  
    Add 'Create Extract Script' menu item for Blob storage files in 'AZURE DATALAKE' Explorer.  
    Add command 'ADL: Create EXTRACT Script' into command palette to auto create extract script for ADL and blob storage files.

## 0.2.13 - 2018-04-20
- Minor fix for telemetry

## 0.2.12 - 2018-04-16
- Add Azure Blob Storage (WASB) Integration -  
    Explore Blob Storage Accounts under Data Lake Compute Account  
    Explore Blob Containers  
    Navigate blob storage files  
    Preview and edit block blob files (up to 4MB)  
    Download blob storage file  
    Upload Blob  
    Delete Blob files  
    Delete blob container
    Copy Blob path
- Rename explorer to 'Azure Datalake'.

## 0.2.11 - 2018-02-14
- Minor fix

## 0.2.10 - 2018-02-09
- Add 'Start U-SQL scripting' command at Datalake Explorer navigation bar.
- Support Job View dark/light theme.
- Fix when extension initialize click 'refresh' on explorer will show error 'command not find'.
- Fix authentication bug when user id not been updated in some corner case in when initialize extension. 

## 0.2.9 - 2018-01-29
- Display job and data details within VSCode for an historical job through command 'ADL: Show job'.
- Add job view and data page for job monitoring within VSCode for both local and ADL jobs.
- Enable job resubmission for an old job. 
- View job U-SQL script for a submitted job.
- Add command 'ADL: Set Default Context' to set default context for current working folder. 
- Fix Azure Account Login extension upgrade related errors.  

## 0.2.8 - 2017-12-22
- Integrate with VSCode Azure Account for improved Azue sign in experiences.
- Enable multi-tenant scenario.  
- Update Data Lake Explorer to be Azure Subscription oritented.
- Add 'Script to Create', ‘Delete’ menu for U-SQL database objects creation and deletion.
- Add ‘Delete’, ‘Upload Folder’ menu for ADLS Storage files and folders.
- Add 'ADL: Set Git Ignore' command to exclude certain system generated files and folders from github respository. 

## 0.2.7 - 2017-11-20
- Support Python code behind for custom code.
- Support R code behind for custom code.
- Integrate ADLA and ADLS with VSCode explorer for better user experiences to access ADLA metadata and perform ADLS data preview, upload and download.
- Improve ADLS file upload and download experiences.  

## 0.2.6 - 2017-10-18
- Minor fix to 0.2.5
- Add ADLS file download capability with status monitoring.
- Improve file upload single or multiple file capabilities with status monitoring.
- Remove Java dependency and .NetCore dependency for Windows.
- Solidify tools performance and reliability through architecture updates.
- Improve user getting started experiences and updated VSCode C# extension installation to be on demand.

## 0.2.5 - 2017-10-13
- Add ADLS file download capability with status monitoring.
- Improve file upload single or multiple file capabilities with status monitoring.
- Remove Java dependency and .NetCore dependency for Windows.
- Solidify tools performance and reliability through architecture updates.
- Improve user getting started experiences and updated VSCode C# extension installation to be on demand.

## 0.2.4 - 2017-07-17
- Minor fix

## 0.2.3 - 2017-07-14
- Implement Local debug in addition to local run for windows users. 
- Enable users to debug your C# code behind, step through the code, validate your script locally before submitting to ADLA.
- Refine VSCode status bar for user's ADLA context information. 
- Display the account|database|schema information on the status bar at the left-bottom of the corresponding USQL file. 
- Enhance metadata navigation for better user experiences. 
- Simplify ADLA metadata navigation based on user's ADLA context. 
- Enable assemblies' registration through Json configuration file. 
- Allow user to register assembly with dependencies and resources through simple configuration settings.
- Enable files upload through Json configuration file. 
- Allow user to upload multiple files through simple configuration settings. 
- Refine show job history view. 
- Offer better experiences for user to view historical jobs. 

## 0.2.2 - 2017-05-14
- Enhance performance for Azure Data Lake Analytics Navigation.
- Improve Performance for Azure Data Lake Storage Integration.
- Optimize process for U-SQL Local Run Dependency Download and Local Run Service Start. 

## 0.2.1 - 2017-05-12
- bug: fix telemetry loss

## 0.2.0 - 2017-05-10
- Local Run for Windows
- ADLS Integration – upload file
- Show Jobs (Including job detail information)
- Language - Smart Indent

## 0.1.13 - 2017-03-07
- Enhance Assembly Registration
- Add ADLS Integration –   
    Preview file, list path, open azure path in web from the command palette  
    Preview file, list path, open azure path in web from the right click menu  
- Enhance Language Service - Go To Definition, Auto Format, Find All
References, Code Snippet
- Open Sample Code

## 0.1.12 - 2017-02-04
- hotkey: Open Sample Script enhancement
- hotkey: List Storage Path
- hotkey: Open Azure Storage in Web
- hotkey: Preview Storage File

## 0.1.10 - 2017-01-10
- Telemetry hotfix 
- hotkey: F12 Goto Definition implemented

## 0.1.8 - 2016-10-11
- U-SQL language sample package.
- U-SQL language editing support, including Syntax Highlighting, IntelliSense, Error Marker, etc.
- U-SQL scripting, code behind programming, compiling and assembly registration. 
- Azure Data Lake Analytics U-SQL job submission, execution and job status monitoring. 
- Azure Data Lake compute account objects navigation, including database, schema, metadata, etc.
