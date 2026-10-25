# DevOps Lab Experiments 5–12

Based on the uploaded DevOps Lab Manual. See each experiment folder for code.

## Requirements
Python 3.12; Docker for Experiments 6–9 and 12; Kubernetes/kubectl for 8–9; Java/Javac for 5; Selenium 4 and Chrome/Chromium for 10–12.

## Local checks
```bash
python -m unittest discover -s experiments-5-12/tests -v
python experiments-5-12/exp07/hello.py
```

Docker/Kubernetes/Selenium integration needs those services and browser drivers installed. Replace `YOUR_DOCKERHUB_USER` in Kubernetes manifests with your pushed image name.