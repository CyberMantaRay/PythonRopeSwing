## Env Setup

<details>
<summary>

#### 0. Minimal

</summary>

- Windows Def. Install Path: `C:\Users\<user> → ~\AppData\Local\Programs\Python`
- [Downloads | VS Code](https://code.visualstudio.com/download)
- [Downloads | Python.org](https://www.python.org/downloads/)

</details>

### 1. Miniconda
- [Miniconda Install](https://www.anaconda.com/docs/getting-started/miniconda/install#basic-install-instructions)
- [Conda Docs | docs.conda.io](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- **App:** Anaconda Prompt
    - Navigate to project folder
    - ```bash      
      conda create --prefix ./env numpy pandas matplotlib scikit-learn jupyter

      conda create -n myenv python
      conda install -n myenv scipy

      conda activate C:\Users\<USER>\<PROJ_DIR>\env
      conda deactivate

      conda install jupyter   # Installs to current active environment
      jupyter notebook

      conda export --prefix .\env > environment.yml
      conda env create -f environment.yml [--name uniq_env_name]
      conda activate uniq_env_name

      conda info --envs
      conda env list
      conda env remove --name myenv
      ```
    - [Conda Cheatsheet (Official)](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
    - [Managing Environments | Conda Docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

