# Lesson

## Brief

### Preparation

Create the conda environment by using the `environment.yml` file.

### Lesson Overview

This lesson introduces `Jupyter Notebook` and `Numpy` library. Jupyter Notebook is a web-based interactive development environment for creating and sharing documents that contain live code, equations, visualizations and narrative text. Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

---

## Part 1 - Introduction to Jupyter Notebook

Install the prescribed conda environment before you begin.

```bash
conda env create -f environment.yml
```

### Jupyter Notebook Demo

To start Jupyter Notebook, open your terminal (or anaconda prompt), then activate the conda environment:

```bash
conda activate pds
```

followed by:

```bash
jupyter notebook
```

This will start the Jupyter Notebook server and open a browser window. You can then navigate to the folder where you want to create a new notebook and click on the `New` button on the top right corner of the page. You can then select `Python 3` to create a new notebook.

> Navigate to the `notebooks` folder in this directory and create a new notebook, name it `jupyter_notebook_demo`.
>
> Then, explore the different features of Jupyter Notebook. Try different command mode actions. Write and execute python code. Write and render markdown. Familiarize with the different keyboard shortcuts.
>
> Save your notebook.

To end the Jupyter Notebook server, go back to the terminal (or anaconda prompt) and press `Ctrl + C` twice.

### Jupyter Notebook extension in VSCode

We installed the Jupyter extension in VSCode in Unit 1. This extension allows us to use Jupyter Notebook in VSCode. To start a Jupyter Notebook server in VSCode, open the command palette (`Ctrl + Shift + P` or `Cmd + Shift + P` on mac), then search for `Jupyter: Create New Blank Notebook`. This will start the Jupyter Notebook server and open a new notebook in VSCode.

> Create a new notebook in VSCode.
>
> In the `Select Kernel`, choose `Python Environments`, then search for `pds` and select it.
>
> Write and execute python code. Write and render markdown. Explore the different features and keyboard shortcuts.
>
> Then save the file in the `notebooks` folder and name it `jupyter_notebook_vscode_demo.ipynb`.

## Part 2 - Introduction to Numpy

We will be using the `notebooks/numpy_lesson.ipynb` notebook for this section. We will be mainly using the Jupyter Notebook extension in VSCode throughout this course as it is more convenient and coherent.

> Open the notebook in VSCode by double clicking on the file. Then select `pds` conda environment for the kernel.
>
> Follow on with the lesson in the notebook.
