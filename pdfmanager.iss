; ============================================================
; TEMPLATE INNO SETUP POUR APPLICATIONS PYTHON
; ============================================================
;
; INSTRUCTIONS :
; 1. Remplacer toutes les valeurs entre [CROCHETS]
; 2. Compiler ton script Python avec PyInstaller :
;    pyinstaller --onedir --windowed --name [NomExe] ton_script.py
; 3. Ouvrir ce fichier avec Inno Setup et compiler (Ctrl+F9)
;
; ============================================================

; ************************************************************
; SECTION SETUP - Paramètres généraux (OBLIGATOIRE)
; ************************************************************
[Setup]

; --- Identité de l'application ---
AppName=PDF_MANAGER
AppVersion=1.0.0
AppPublisher=Uriel_Yechi
;AppPublisherURL=[https://ton-site.com]
;AppSupportURL=[https://ton-site.com/support]

; --- Dossiers ---
; {autopf} = Program Files adapté automatiquement (32/64 bits)
DefaultDirName={autopf}\[NomDossier]
DefaultGroupName=PDF_MANAGER

; --- Fichier installateur généré ---
OutputDir=installer_output
OutputBaseFilename=[NomApp]_Setup_[1.0.0]

; --- Compression (choisir une option) ---
; zip = rapide, fichier plus gros
; lzma = lent, fichier plus petit
Compression=lzma
SolidCompression=yes

; --- Icône de l'installateur (optionnel, supprimer si pas d'icône) ---
; SetupIconFile=C:\Users\edyec\Downloads\pdfmanage\Logopdfmanager.ico

; --- Privilèges ---
; lowest = pas besoin d'admin (installe dans AppData si pas les droits)
; admin = nécessite les droits admin
PrivilegesRequired=lowest

; --- Infos version Windows (optionnel) ---
VersionInfoVersion=1.0.0
VersionInfoCompany=Uriel DEV
VersionInfoDescription=Application de gestion de pdfs

; ************************************************************
; SECTION LANGUAGES - Langues de l'installateur (OPTIONNEL)
; ************************************************************
[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

; ************************************************************
; SECTION TASKS - Options pour l'utilisateur (OPTIONNEL)
; ************************************************************
[Tasks]
; Case à cocher pour créer un raccourci bureau
Name: "desktopicon"; Description: "Créer un raccourci sur le Bureau"; Flags: unchecked

; ************************************************************
; SECTION FILES - Fichiers à installer (OBLIGATOIRE)
; ************************************************************
;[Files]

; --- Application principale (générée par PyInstaller) ---
; Adapter le chemin selon ton projet
Source: "dist\PDF MANAGER\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; --- Fichiers supplémentaires (optionnel, décommenter si besoin) ---
; Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion
; Source: "assets\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
; Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs

; ************************************************************
; SECTION ICONS - Raccourcis (OPTIONNEL mais recommandé)
; ************************************************************
[Icons]

; --- Menu Démarrer ---
Name: "{group}\PDF MANAGER"; Filename: "{app}\PDF MANAGER.exe"
Name: "{group}\Désinstaller PDF MANAGER"; Filename: "{uninstallexe}"

; --- Bureau (seulement si l'utilisateur a coché la case) ---
Name: "{autodesktop}\PDF MANAGER"; Filename: "{app}\PDF MANAGER.exe"; Tasks: desktopicon

; ************************************************************
; SECTION RUN - Actions après installation (OPTIONNEL)
; ************************************************************
[Run]

; Proposer de lancer l'application après installation
Filename: "{app}\PDF MANAGER.exe"; Description: "Lancer PDF MANAGER"; Flags: postinstall nowait skipifsilent

; ************************************************************
; SECTION UNINSTALLDELETE - Nettoyage désinstallation (OPTIONNEL)
; ************************************************************
[UninstallDelete]

; Supprimer les fichiers créés par l'application (logs, cache, etc.)
 Type: filesandordirs; Name: "{app}\logs"
 Type: filesandordirs; Name: "{app}\cache"


; ============================================================
; SECTIONS AVANCÉES (décommenter si besoin)
; ============================================================

; ************************************************************
; SECTION REGISTRY - Modifications registre (OPTIONNEL)
; ************************************************************
; [Registry]
; ; Exemple : sauvegarder un paramètre
; Root: HKCU; Subkey: "Software\[NomApp]"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"

; ************************************************************
; SECTION CODE - Scripts Pascal (OPTIONNEL, avancé)
; ************************************************************
; [Code]
; // Exemple : afficher un message personnalisé
; procedure InitializeWizard();
; begin
;   MsgBox('Bienvenue dans l''installation !', mbInformation, MB_OK);
; end;
