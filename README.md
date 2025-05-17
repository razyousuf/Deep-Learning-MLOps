# Deep-Learning-MLOps

## Workflow

1. Update the config.yaml # changeble vars and urls
2. Update the params.yaml & read it
3. Update the entity & read it
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py # Create Enpoints
8. Update the dvc.yaml

## How to run?

```bash
conda create -n chest python=3.8 -y
```

```bash
conda activate chest
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag
