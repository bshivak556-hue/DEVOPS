# DevOps Lab Execution Report — Experiments 5–12

## Checks completed in the available execution environment

- Experiment 5 Java program: **PASS** — compiled with `javac` and printed `Hello from Jenkins CI!`.
- Experiment 7 Python program: **PASS** — printed `Hello World`.
- Python syntax compilation for the available Python scripts: **PASS**.
- Experiments 8 and 9 Kubernetes YAML: **PASS** — deployment and service manifests parsed successfully.
- Python unit test suite: **PASS** — 1 test passed.

## Integration checks not run here

This execution environment does not have Docker or kubectl installed. Flask and Selenium Python packages are also not installed here, and the environment cannot download packages from the internet. Therefore, Docker image builds, Kubernetes deployments, Jenkins server execution, and real-browser Selenium tests are **not verified** by this report.

## Run on a machine with the tools installed

From the repository root:

```powershell
python -m pip install -r experiments-5-12/requirements.txt
python -m unittest discover -s experiments-5-12/tests -v
javac experiments-5-12/exp05/Hello.java -d build
java -cp build Hello
python experiments-5-12/exp07/hello.py
docker build -t devops-hello:latest experiments-5-12/exp07
docker run --rm devops-hello:latest
```

For experiments 8–9, replace `YOUR_DOCKERHUB_USER` in the Kubernetes manifests with a published image name, build and push the image, and ensure a Kubernetes cluster is running before applying the manifests. Selenium tests require a working Chrome/Chromium browser and Selenium-compatible driver/runtime.
