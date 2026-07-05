; ============================================================
; EXEMPLE : Application "MaCalculatrice"
; ============================================================
; Ceci est un exemple concret du template rempli
; ============================================================

[Setup]
AppName=Ma Calculatrice
AppVersion=1.0.0
AppPublisher=Uriel Dev
AppPublisherURL=https://github.com/uriel
DefaultDirName={autopf}\MaCalculatrice
DefaultGroupName=Ma Calculatrice
OutputDir=installer_output
OutputBaseFilename=MaCalculatrice_Setup_1.0.0
Compression=zip
SolidCompression=yes
PrivilegesRequired=lowest
VersionInfoVersion=1.0.0
VersionInfoCompany=Uriel Dev
VersionInfoDescription=Une calculatrice simple

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "Créer un raccourci sur le Bureau"; Flags: unchecked

[Files]
Source: "dist\MaCalculatrice\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Ma Calculatrice"; Filename: "{app}\MaCalculatrice.exe"
Name: "{group}\Désinstaller Ma Calculatrice"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Ma Calculatrice"; Filename: "{app}\MaCalculatrice.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\MaCalculatrice.exe"; Description: "Lancer Ma Calculatrice"; Flags: postinstall nowait skipifsilent
