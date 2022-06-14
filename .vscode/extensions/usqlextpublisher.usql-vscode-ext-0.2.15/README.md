## Microsoft Azure Data Lake Tools for Visual Studio Code

Azure Data Lake Tools for VSCode - an extension for developing U-SQL projects against [Microsoft Azure Data Lake](https://azure.microsoft.com/en-us/solutions/data-lake/)!

This extension provides you a cross-platform, light-weight, keyboard-focused authoring experience for U-SQL while maintaining a rich set of development functions.

### New features:
* Auto Create extract script -
    * Add 'Create Extract Script' menu item for .txt, .csv and .tsv files in AZURE DATALAKE Explorer
    * Add command 'ADL: Create EXTRACT Script' for ADL and blob storage files.

### Primary features:

* Integrate with VSCode Azure Account for Azue sign in integration and enable multi-tenant Azure scenario.
* Set default ADL context for current working folder through command 'ADL: Set Default Context'.
* Exclude system generated files and folders from github respository through command 'ADL: Set Git Ignore'.
* Built-in U-SQL language service - including Syntax Highlighting, IntelliSense, Auto Format, Go To Definition, Find All References, Error Markers, Code Snippet, etc.
* Include U-SQL sample package for quick start.
* Support U-SQL scripting and assembly registration.
* Support U-SQL code behind programming with C#, Python and R. 
* Support U-SQL local run & local debug in windows.
* Enable U-SQL Azure Data Lake Analytics job submission with job execution and job status Monitoring.

* Azuer Data Lake Job Management -
    * Display job summary and data information for running job monitoring.
    * View job and data details for an historical job through command 'ADL: Show job'.
    * Enable job resubmission for an old job.
    * View job U-SQL script for a submitted job.

* Azuer Data Lake Analytics Integration -
    * U-SQL metadata navigation for objects such as databases, schemas, table, Index and other metadata objects through explorer or commands. 
    * U-SQL metadata objects creation and deletion through VSCode Data Lake Explorer. 
    * Show ADLA historical jobs.

* Azure Data Lake Storage Integration -
    * ADLS folder and file exploration, file preview, file download and file/folder upload through commands.
    * ADLS folder and file exploration, file preview, file download, file/folder delete and file/folder upload through VSCode Data Lake Explorer.

* Azure Blob Storage Integration -
    * Blob Storage folder and file exploration, file preview, file download, file/folder delete and file upload through VSCode Data Lake Explorer.

### Runtime prerequisites for macOS and Linux:
* [.NET Core 2.0](https://www.microsoft.com/net/download/core)
* [Mono 5.2.X](http://www.mono-project.com/download/)

### Offline Installation

Azure Data Lake extension will download and install required dependencies during activation. For machines with no Internet access, you can install the extension and dependencies by choosing the **Install from VSIX...** option in the Extension view and installing a bundled release from the [releases page](true/https:\github.com\Microsoft\AzureDatalakeToolsForVSCode\releases). Each operating system has a .vsix file with the required service included. Pick the file for your OS, download and install to get started.

### Quick Start
**Azure Data Lake Tools for VSCode will only be activated when you either create a new U-SQL File or open an existing U-SQL file.**
**You can activate Azure Data Lake Tools for VSCode via creating a new U-SQL File or opening an existing U-SQL file with extension of .usql. You can also press F1, type 'Change Language Mode', and then choose USQL (usql) to enable the ADL Extension.**

* How to login into Azure(ADL: Login)

![Login Azure](https://usqldownload.blob.core.windows.net/ext/Login.gif)

* How to use Data Lake Explorer to manage ADLA metadata

![U-SQL Database](https://usqldownload.blob.core.windows.net/ext/ExplorerADLA.gif)

* How to use Data Lake Explorer to manage ADLS resources

![ADLS Files](https://usqldownload.blob.core.windows.net/ext/ExplorerADLS.gif)

* How to use Data Lake Explorer to manage blob storage resources

![Blob Files](https://usqldownload.blob.core.windows.net/ext/ExplorerBlob.gif)

* How to open U-SQL sample script (ADL: Open Sample Script)

![Open Usql Sample](https://usqldownload.blob.core.windows.net/ext/OpenUsqlSample.gif)

* How to open a U-SQL working folder

![Open Usql Folder](https://usqldownload.blob.core.windows.net/ext/OpenFolder2.gif)

* How to preview an ADLS file through right clicking on a path string

![Preview File](https://usqldownload.blob.core.windows.net/ext/Preview.gif)

**Local Run for Windows** – Allow you to perform local run to test your local data, validate your script locally before publishing your production ready code to ADLA.

* Use command ADL: Start Local Run Service to start local run service. The cmd console shows up. For first time users, enter 3 and set up your data root.

![StartLocalRunSvc](https://usqldownload.blob.core.windows.net/ext/StartLocalRunSvc.png)

* Use command ADL: Submit Job to submit your job to your local account.

![SubmitJobToLocal](https://usqldownload.blob.core.windows.net/ext/SubmitJobToLocal.png)

* After job submission, you can view the submission details by clicking jobUrl in the output window or view the job submission status from the CMD console.

![ViewJobInfo1](https://usqldownload.blob.core.windows.net/ext/ViewJobInfo1.png)

![ViewJobInfo2](https://usqldownload.blob.core.windows.net/ext/ViewJobInfo2.png)

**Local Debug for Windows** - Enable you to debug your C# code behind, step through the code, validate your script locally before submitting to ADLA.

* Prerequisites: Follow the reminders to install [.NET Core 2.0](https://www.microsoft.com/net/download/core) and [C# for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.csharp).
* Use command ADL: Start Local Run Service to start local run service, set a breakpoint in your code behind, then click command ADL: Local Debug to start local debug service.  You can debug through the debug console and view parameter, variable and call stack information.

![LocalDebugCodeBehind](https://usqldownload.blob.core.windows.net/ext/LocalDebugCodeBehind.png)

* How to submit a U-SQL job locally

![Local Run](https://usqldownload.blob.core.windows.net/ext/LocalRun.gif)

* Video: [Azure Data Lake Tools for Visual Studio Code](true/https:\channel9.msdn.com\Series\AzureDataLake\Azure-Data-Lake-Tools-for-VSCode)
* User Manual: [Use the Azure Data Lake Tools for Visual Studio Code](https://docs.microsoft.com/en-us/azure/data-lake-analytics/data-lake-analytics-data-lake-tools-for-vscode)

### Azure Data Lake Commands
* Press **F1** or **Ctrl**+**Shift**+**P** to open Visual Studio Code Command Palette
* Enter ADL: to list the customized commands, which begin with "**ADL:**" prefix.

#### Customized commands:
* ADL: Generate Code Behind – Create a code-behind file with the same name as the U-SQL file for authoring C# extensions
* ADL: Open Sample Script – Open and view a U-SQL Sample script
* ADL: Register Assembly – Register custom code assembly into the ADLA metadata store
* ADL: Set Script Parameters – Set up ADLA account and job execution parameters (e.g. parallelism, runtime, etc.)
* ADL: Compile Script – Submit U-SQL file and code behind (if any) to ADLA for compilation
* ADL: Submit Job – Submit U-SQL job to ADLA for execution
* ADL: Start Local Run Service – Open U-SQL Local Run Service in Windows.
* ADL: Show Job – Display historical jobs

#### Azure Data Lake Metadata Navigation to view different objects:
* ADL: List Accounts
* ADL: List Assemblies
* ADL: List Credentials
* ADL: List Databases
* ADL: List External Data Sources
* ADL: List Procedures
* ADL: List Schemas
* ADL: List Table Partitions
* ADL: List Table Statistics
* ADL: List Table Types
* ADL: List Table Valued Functions
* ADL: List Tables
* ADL: List Types
* ADL: List Views

#### Azure Data Lake Store Integration
* ADL: List ADLS Path
* ADL: Preview ADLS File
* ADL: Upload Data to ADLS
* ADL: Download Data from ADLS
* ADL: Open Azure Storage Explorer

### Supported Operating Systems
* Windows
* macOS
* Ubuntu 14.04

### More information
* For the getting started information on Data Lake Analytics, see [Tutorial: get started with Azure Data Lake Analytics](https://docs.microsoft.com/en-us/azure/data-lake-analytics/data-lake-analytics-get-started-portal).
* For information on using Data Lake Tools for Visual Studio, see [Tutorial: develop U-SQL scripts using Data Lake Tools for Visual Studio](https://docs.microsoft.com/en-us/azure/data-lake-analytics/data-lake-analytics-data-lake-tools-get-started).

### Found a Bug?
* contact <mailto:adldevtool@microsoft.com>
* https://github.com/Microsoft/AzureDatalakeToolsForVSCode/issues

### Contributions
* Want to make this extension even more awesome? [Share your feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR8qR1up5nRdNilGZWj_t-wBUOUxYTUVKUlYzTUQzUUFTOEZXRVVVR0hMMC4u).

### Offline Installation

The extension will download and install a required language service package during activation. For machines with no Internet access, you can still use the extension by choosing the Install from VSIX... option in the Extension view and installing a bundled release from our [releases](https://github.com/Microsoft/AzureDatalakeToolsForVSCode/releases) page. Each operating system has a .vsix file with the required service included. Pick the file for your OS, download and install to get started.

License

The Microsoft Azure Data Lake Tools extension is subject to [these license terms](https://github.com/Microsoft/AzureDatalakeToolsForVSCode/blob/master/LICENSE).