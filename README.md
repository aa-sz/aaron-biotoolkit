# aaron-biotoolkit

This is my personal toolkit for easy and fast biological files manipulation.

*[Instrucciones en español disponibles al final](#aaron-biotoolkit-español)*

## afs2pdb
This tool makes the process of converting an AlphaFold Server file to a PDB file fast, consuming directly the .zip file to a .pdb file, eliminating the need of unzipping, file selection, and mmCIF to PDB file conversion, all in one command.

### Usage
> afs2pdb [PATH]

By default, afs2pdb will generate a .pdb file with the same name as the .zip file. If you want to specify the output filename that you want, use the `-o` option.
>afs2pdb [PATH] -o [OUTPUT_FILENAME]

## Installation
This package is intended to be installed using **[pipx](https://github.com/pypa/pipx)**. This is to isolate the dependencies and avoid collisions with other Python packages installed in the system.

### Windows
1. Install the latest version of **[Python](https://www.python.org/downloads/)** (skip if already installed, Python 3.8+ is required).
2. Install pipx:
   ```
   python -m pip install --user pipx
   python -m pipx ensurepath
   ```
3. Install aaron-biotoolkit from GitHub:
   ```
   pipx install git+https://github.com/aa-sz/aaron-biotoolkit
   ```

### macOS
1. Install the latest version of Python (skip if already installed):
   ```
   brew install python
   ```
   If you don't have Homebrew installed, visit [brew.sh](https://brew.sh) for installation instructions.
2. Install pipx:
   ```
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```
3. Install aaron-biotoolkit from GitHub:
   ```
   pipx install git+https://github.com/aa-sz/aaron-biotoolkit
   ```

### Linux
1. Install Python 3.8+ (skip if already installed):
   ```
   # Debian/Ubuntu
   sudo apt update
   sudo apt install python3 python3-pip
   
   # Fedora
   sudo dnf install python3 python3-pip
   ```
2. Install pipx:
   ```
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```
3. Install aaron-biotoolkit from GitHub:
   ```
   pipx install git+https://github.com/aa-sz/aaron-biotoolkit
   ```

## Uninstallation
To uninstall aaron-biotoolkit:
```
pipx uninstall aaron-biotoolkit
```

---

# aaron-biotoolkit (Español)

Este es mi conjunto de herramientas personal para una manipulación fácil y rápida de archivos biológicos.

## afs2pdb
Esta herramienta hace que el proceso de convertir un archivo de AlphaFold Server a un archivo PDB sea rápido, consumiendo directamente el archivo .zip para generar un archivo .pdb, eliminando la necesidad de descomprimir, seleccionar archivos y convertir de mmCIF a PDB, todo en un solo comando.

### Uso
> afs2pdb [RUTA]

Por defecto, afs2pdb generará un archivo .pdb con el mismo nombre que el archivo .zip. Si deseas especificar el nombre del archivo de salida, usa la opción `-o`.
>afs2pdb [RUTA] -o [NOMBRE_ARCHIVO_SALIDA]

## Instalación
Este paquete está diseñado para ser instalado usando **[pipx](https://github.com/pypa/pipx)**. Esto es para aislar las dependencias y evitar colisiones con otros paquetes de Python instalados en el sistema.

### Windows
1. Instala la última versión de **[Python](https://www.python.org/downloads/)** (omite si ya está instalado, se requiere Python 3.8+).
2. Instala pipx:
   ```
   python -m pip install --user pipx
   python -m pipx ensurepath
   ```
3. Instala aaron-biotoolkit desde GitHub:
   ```
   pipx install git+https://github.com/aa-sz/aaron-biotoolkit
   ```

### macOS
1. Instala la última versión de Python (omite si ya está instalado):
   ```
   brew install python
   ```
   Si no tienes Homebrew instalado, visita [brew.sh](https://brew.sh) para instrucciones de instalación.
2. Instala pipx:
   ```
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```
3. Instala aaron-biotoolkit desde GitHub:
   ```
   pipx install git+https://github.com/aa-sz/aaron-biotoolkit
   ```

### Linux
1. Instala Python 3.8+ (omite si ya está instalado):
   ```
   # Debian/Ubuntu
   sudo apt update
   sudo apt install python3 python3-pip
   
   # Fedora
   sudo dnf install python3 python3-pip
   ```
2. Instala pipx:
   ```
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```
3. Instala aaron-biotoolkit desde GitHub:
   ```
   pipx install git+https://github.com/aa-sz/aaron-biotoolkit
   ```

## Desinstalación
Para desinstalar aaron-biotoolkit:
```
pipx uninstall aaron-biotoolkit
```
