# Conda

## Miniconda
Download and install [minconda](https://docs.conda.io/en/latest/miniconda.html). On Windows open the Anaconda Prompt. On Mac or Linux open Terminal.

## Spyder
Install the Spyder IDE in a dedicated environment.
```
conda init bash
conda update -n base conda
conda config --env --set channel_priority strict
conda create -c conda-forge -n spyder-env spyder numpy scipy pandas matplotlib sympy cython
conda activate spyder-env
```

Activate the environment and run Spyder.
```
conda activate spyder-env
spyder
```

Plugins:
```
conda install -c conda-forge spyder-terminal spyder-notebook
```

## Computational Design Environment
Create a new environment and install the neccessary packages.
```
conda create --name computational-design
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install -c conda-forge spyder-kernels
conda install -c conda-forge scipy
conda install -c conda-forge seaborn
conda install -c conda-forge rasterio
conda install -c conda-forge lazrs-python
conda install -c conda-forge laspy
conda install -c conda-forge pyntcloud
conda install -c conda-forge pyvista
```

Or as a one liner:
```
conda create -n computational-design -c conda-forge spyder-kernels scipy seaborn rasterio lazrs-python laspy pyntcloud pyvista viscm colorspacious cmcrameri cmasher colorcet cmocean
```

Then use Pip to install packages that are not available through Conda. The package [pyfastnoisesimd](https://pypi.org/project/pyfastnoisesimd/) requires Microsoft Visual C++ 14.0 or greater. Go to [C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Download and run Visual Studio Build Tools installer. In the installer, check `Desktop development with C++` and then install.

```
conda activate computational-design
pip install lidario
pip install pyfastnoisesimd
pip install cellpylib
```

Or as one liner:
```
conda activate computational-design
pip install lidario pyfastnoisesimd cellpylib
```

Set this environment as the Python interpreter for Spyder. First find the Python path of the environment with `where python`. Activate the Spyder environment, start Spyder, open its preferences, and set this path for the Python interpreter. Restart Spyder.
```
where python
conda deactivate
conda activate spyder-env
spyder
```

Path: 
```
C:\Users\baharmon\AppData\Local\miniconda3\envs\computational-design\python.exe
```

## Earth Analytics

```
conda create -n computational-design -c conda-forge spyder-kernels scipy 
conda install -c conda-forge earthpy
```
Alternatively install with pip:
```
pip install earthpy
```

## Lidar
* [lasypy](https://github.com/laspy/laspy)
* [pyvista](https://docs.pyvista.org/)
* [open3d](http://www.open3d.org/)

```
conda create --name lidar
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install -c conda-forge spyder-kernels lazrs-python laspy numpy pyvista pyntcloud seaborn
```

Path:
```
C:\Users\baharmon\AppData\Local\miniconda3\envs\lidar\python.exe
```

## Open3D

```
conda create -n open3d -c conda-forge -c open3d-admin open3d spyder-kernels
```


Path:
```
C:\Users\baharmon\AppData\Local\miniconda3\envs\open3d\python.exe
```

## Colors

```
conda create -n colors -c conda-forge spyder-kernels seaborn cmcrameri cmasher colorcet viscm colorspacious cmocean
```

Path:
```
C:\Users\baharmon\AppData\Local\miniconda3\envs\colors\python.exe
```

## Experimental

```
conda create -n experimental -c conda-forge spyder-kernels scipy seaborn rasterio lazrs-python laspy pyntcloud pyvista viscm colorspacious cmcrameri cmasher colorcet cmocean
conda activate experimental
pip install lidario pyfastnoisesimd cellpylib
```
Remove environment:
```
conda remove -n experimental --all
```

## Environment Packaging
* YAML
* Conda Pack
* see: https://www.anaconda.com/blog/moving-conda-environments

## TODO
* [ ] Package environment
* [ ] Test with spyder binaries




