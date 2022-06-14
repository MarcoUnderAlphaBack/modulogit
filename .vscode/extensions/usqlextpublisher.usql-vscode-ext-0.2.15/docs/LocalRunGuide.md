# Set up USQL LocalRun Environment

## Download Localrun Dependency 
- Use Command **ADL: Download LocalRun Dependency** to download the packages  

![DownloadLocalRun](.\images\1_DownloadLocalRun.png)

## Install Dependency Packages
locate the Dependency packages by checking the log outputs, eg:  
`C:\Users\xxx\.vscode\extensions\usqlextpublisher.usql-vscode-ext-x.x.x\LocalRunDependency
`  
![LocateDependency](.\images\2_LocateDependencyPath.png)

- Install BuildTools  

![InstallBuildTools](.\images\3_InstallBuildTools.png)
- Install Win10SDK 10240  

![InstallWin10SDK](.\images\4_InstallWin10SDK.png)
- Setup environment variable, Set the **SCOPE_CPP_SDK** environment variable to:  
`C:\Users\xxx\AppData\Roaming\LocalRunDependency\CppSDK_3rdparty
`  
Make sure to restart OS to make the environment variable settings take effect  

![ConfigSCOPE_CPP_SDK](.\images\5_ConfigScopeCppSDk.png)

# Start Local Run Server
- Use Command **ADL: Start Local Run Service** to start local run service  

![StartLocalRunService](.\images\6_StartLocalRunSvc.png)

# Submit USQL job to local run Server
- Submit job by using command **ADL: Submit Job**