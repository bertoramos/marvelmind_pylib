
<!--
# Debug execute

1. Install Visual Studio Code
2. Install Blender Development Extension : https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development
3. Install utilities addon in Blender.
3. Open drone_control folder with VSC.
4. Press CTRL-SHIFT-P, execute Blender Start and select Blender executable. Blender will open automatically.

-->

<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/bertoramos/drone_assistant">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">marvelmind_pylib</h3>

  <p align="center">
    Python binding for Marvelmind C API
    <br />
    <a href="https://github.com/bertoramos/marvelmind_pylib"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/bertoramos/marvelmind_pylib/issues">Report Bug</a>
    ·
    <a href="https://github.com/bertoramos/marvelmind_pylib/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<br>

---

<!-- ABOUT THE PROJECT -->
## About The Project

Python binding for Marvelmind C API

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Marvelmind C Library](https://github.com/MarvelmindRobotics/marvelmind.c)
- [pybind11](https://github.com/pybind/pybind11)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

- Python 3
- [Marvelmind IPS](https://marvelmind.com)

### Installation

```bash
$ python pip install https://github.com/bertoramos/marvelmind_pylib/releases/download/{version}/{so-version-file}.whl
```

### Install from source

#### Building

##### Unix

TODO

##### Windows

1. Install Visual Studio.
2. Create a python virtual environment and install pybind11.

    ```bash
    $ conda create --prefix .\.venv python=3.11
    $ conda activate .\.venv
    $ python -m pip install --upgrade pip
    (.\.venv) $ python -m pip install pybind11
    ```

3. Run win_make.bat to build library.

4. A file with extension .pyd must have been created. You can find it in *makefiles/win_build/Release* folder.

##### Installation

1. Copy the .pyd file inside makefiles/marvelmind_pylib/marvelmind_pylib folder.
2. Modify version and requires-python parameters pyproject.toml file.

```toml
version = "1.0.0"
requires-python = ">=3.11"
```

3. Build wheel:

```bash
  (.\.venv) $ python -m pip install build
  (.\.venv) $ python -m build
``

4. Install wheel. Inside makefiles/marvelmind_pylib/dist folder you will find the wheel and tar files, ready to be installed.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

This is an example of the use of the library.

```python

import marvelmind_pylib

SERIAL_PORT = "COM5"

dev = marvelmind_pylib.MarvelMindDevice(SERIAL_PORT, True)
dev.start()

while True:
    try:
        mob_pos = dev.getMobileBeaconsPosition()
        stat_pos = dev.getStationaryBeaconsPosition()

        if len(mob_pos) > 0:
            print(mob_pos)
        if len(stat_pos) > 0:
            print(stat_pos)
    except KeyboardInterrupt:
        break

dev.close()

```

### Portable usage

You can [compile](#building) or [download the dynamic .so/.pyd file](https://github.com/bertoramos/marvelmind_pylib/releases) and place it in the same folder as the python script that imports the marvelmind_pylib library.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Alberto Ramos Sánchez - [alberto.ramos104@alu.ulpgc.es](mailto:alberto.ramos104@alu.ulpgc.es)

<p align="right">(<a href="#top">back to top</a>)</p>


<!--

# C Marvelmind API Binding

## Building

### Build marvelmind original sample

1. Create a build folder in original_sample folder
2. In build folder execute : cmake ..
3. In build folder execute : make

### Build marvelmind c++ test program (Unix)

1. Create a build folder in test_marvelmind_device folder
2. In build folder execute : cmake ..
3. In build folder execute : make

### Build marvelmind_pylib (Unix)

1. Create a python virtual environment and install pybind11
2. In marvelmind_pylib folder create a build folder
3. In build folder execute : cmake .. -Dpybind11_DIR=$(python -m pybind11 --cmakedir)
4. In build folder execute : make

### Build marvelmind_pylib (Windows)

1. Install Visual Studio.
2. Create a python virtual environment and install pybind11.
3. In marvelmind_pylib folder create a build folder.
4. In build folder execute : cmake ..
5. In build folder execute : cmake --build . --config Release --target marvelmind_pylib

## Install

### Install in python

1. Execute : python -m ensurepip
2. Execute : python -m pip install --upgrade pip
3. In marvelmind_pylib_setup execute : python -m pip install .


## Pre-build install

1. Execute ./python pip install https://github.com/bertoramos/marvelmind_pylib/releases/download/{version}/{so-version-file}.zip

-->
