# 📅 Week 6: [Web deployment & Model serving]

## 🛠️ 1. What I Built
- **Summary**: This week I deployed a trained text-classification model as a web service using FastAPI and containerized it with Docker for reproducibility. I also built a Streamlit front-end that communicates with the API. The workflow connected three layers — FastAPI as the backend, Streamlit as the user interface, and the trained scikit-learn model stored in models/. I first saved the classifier and vectorizer with joblib, then created src/api.py to expose /predict and /health endpoints. After confirming the API locally via PowerShell requests, I built a Docker image (myapi:env), ran it successfully, and finally pushed the image to Docker Hub as sooyyy/myapi:latest. The week concluded with running src/app.py via Streamlit to display live predictions through the FastAPI backend.
- **Key Tools Used**: FastAPI, Uvicorn, Docker Desktop (WSL2), Streamlit, PowerShell, requests, joblib, scikit-learn, VS Code, GitHub Actions
- **Artifact Location**:
  - https://github.com/tcsai/portfolio-25-26-Sy-Lyy
  - https://hub.docker.com/repository/docker/sooyyy/myapi/general
**How to Run** (if applicable)
- (1) Start FastAPI server : 
uvicorn src.api:app --reload --port 8000
- (2) Test endpoints (PowerShell) : 
Invoke-RestMethod "http://localhost:8000/health"
$body = @{ text = "the grand design" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/predict" -ContentType "application/json" -Body $body
- (3) Build & run Docker container :
docker build -t myapi:env .
docker run --rm -it -p 8000:8000 --env-file .env myapi:env
- (4) Run Streamlit front-end : 
streamlit run src/app.py


## 🔍 2. My Exploration
- **What I Investigated Further**:
- Why PowerShell curl fails while Bash examples work → in PowerShell, curl is an alias for Invoke-WebRequest, which ignores -X, -d, and -H; using curl.exe or Invoke-RestMethod fixes this.
- How to debug connection errors → API wasn’t running; once uvicorn started, /health returned {"status": "RMD-OK"}.
- Docker build failure (_ping 500 error) → caused by stopped WSL instance; fixed by launching Docker Desktop and verifying wsl -l -v → Ubuntu Running.
- Tagged and pushed Docker image to Docker Hub after authenticating with docker login.
- Learned to run Streamlit only via streamlit run instead of python app.py to avoid “missing ScriptRunContext” warnings.
- **Link to Evidence**
- <img width="1902" height="707" alt="image" src="https://github.com/user-attachments/assets/83ff6c14-d961-4735-91a6-fd100abbcf76" />
- <img width="935" height="630" alt="image" src="https://github.com/user-attachments/assets/2ddfd9ef-d9f0-4920-90a5-3cca1d6ac4d0" />
- https://github.com/tcsai/portfolio-25-26-Sy-Lyy
- https://hub.docker.com/repository/docker/sooyyy/myapi/general


## 🤖 3. Use of GenAI (if applicable)
- **What I Asked It To Do**
- Explain why curl commands failed in PowerShell and how to translate them.
- Diagnose Docker build and WSL connection errors.
- Verify correct file locations (src/api.py, models/model.pkl).
- Guide FastAPI, Docker, and Streamlit integration and debugging.
  - ## GenAI Usage Log
- 2025-10-10: Resolved Docker daemon & WSL2 issues.
- 2025-10-10: Debugged FastAPI server connection and endpoint errors.
- 2025-10-10: Helped tag/push Docker image and run Streamlit properly.

- **What I Got and Did With It**:
- Converted Bash-style curl to PowerShell-friendly Invoke-RestMethod.
- Restarted Docker Desktop and verified daemon health.
- Successfully pushed image to Docker Hub and tested Streamlit frontend.
- **Risks or Misuses You Noticed**: While using ChatGPT to connect FastAPI, Docker, and Streamlit, I noticed that it was easy to follow the steps mechanically without fully understanding how each part interacted. The AI’s instructions were helpful, but because it handled several layers at once(backend setup, containerization, and UI integration). I sometimes lost sight of what was happening under the hood. This made me realize how important it is to slow down, test each module separately, and make sure I actually understand the connections before combining everything into one workflow.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?**
- FastAPI and Docker enable the model to run anywhere independent of the local Python setup.
- The .env and Dockerfile guarantee consistent runtime parameters and dependencies.
- The Streamlit layer proves that the API is fully reusable for interactive interfaces or future web integration.
- **What was most confusing or interesting?**
- Discovering that PowerShell’s curl is not real curl.
- Docker’s dependency on a running WSL backend and how restarting Docker Desktop immediately resolved the build failure.
- Streamlit warnings (missing ScriptRunContext) when executed without its CLI.
- **If someone else looked at your repo, what would help them use this part of the project?**
- Clear README instructions for PowerShell users showing Invoke-RestMethod syntax.
- Include .env.example and sample Docker commands for fast reproduction.
- Ensure FastAPI and Streamlit ports don’t conflict when running together (8000 vs 8501).
<details>
<summary>View Execution Logs</summary>

```
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> mkdir models

```
디렉터리: C:\\Users\\수영\\Desktop\\Tilburg Univ\\study\\RM\\portfolio-25-26-Sy-Lyy

```

Mode                 LastWriteTime         Length Name

---

d-----      2025-10-09   오후 7:32                models

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> uvicorn src.api:app --reload --port 8000
INFO:     Will watch for changes in these directories: ['C:\\Users\\수영\\Desktop\\Tilburg Univ\\study\\RM\\portfolio-25-26-Sy-Lyy']
INFO:     Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000/) (Press CTRL+C to quit)
INFO:     Started reloader process [14356] using StatReload
INFO:     Started server process [19412]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> $body = @{ text = "the grand design" } | ConvertTo-Json
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Invoke-RestMethod -Method Post -Uri "http://localhost:8000/predict" -ContentType "application/json" -Body $body

## prediction

science

(.venv) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> curl.exe http://localhost:8000/health
{"status":"RMD-OK"}

(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> & "C:/Users/수영/Desktop/Tilburg Univ/study/RM/portfolio-25-26-Sy-Lyy/.venv/Scripts/Activate.ps1"
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker build -t myapi .
ERROR: error during connect: Head "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/_ping": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker build -t myapi .
[+] Building 521.4s (11/11) FINISHED                                                                                                                                                  docker:desktop-linux
=> [internal] load build definition from Dockerfile                                                                                                                                                  0.1s
=> => transferring dockerfile: 446B                                                                                                                                                                  0.0s
=> [internal] load metadata for [docker.io/library/python:3.11.13-slim](http://docker.io/library/python:3.11.13-slim)                                                                                                                                2.5s
=> [auth] library/python:pull token for [registry-1.docker.io](http://registry-1.docker.io/)                                                                                                                                         0.0s
=> [internal] load .dockerignore                                                                                                                                                                     0.1s
=> => transferring context: 164B                                                                                                                                                                     0.0s
=> [1/5] FROM [docker.io/library/python:3.11.13-slim@sha256:9bffe4353b925a1656688797ebc68f9c525e79b1d377a764d232182a519eeec4](http://docker.io/library/python:3.11.13-slim@sha256:9bffe4353b925a1656688797ebc68f9c525e79b1d377a764d232182a519eeec4)                                                                         35.3s
=> => resolve [docker.io/library/python:3.11.13-slim@sha256:9bffe4353b925a1656688797ebc68f9c525e79b1d377a764d232182a519eeec4](http://docker.io/library/python:3.11.13-slim@sha256:9bffe4353b925a1656688797ebc68f9c525e79b1d377a764d232182a519eeec4)                                                                          0.1s
=> => sha256:b25238518c0cca0928b2117b90cee455c3fbdb7d605f92131e5cc92fbfb5b468 249B / 249B                                                                                                            0.5s
=> => sha256:8c7716127147648c1751940b9709b6325f2256290d3201662eca2701cadb2cdf 29.78MB / 29.78MB                                                                                                     17.8s
=> => sha256:4dc2c3222cdbf7b5e9d5c68653d42c7289ddf2bfaa17b12c961014755b7d04dd 14.64MB / 14.64MB                                                                                                      6.7s
=> => sha256:44350d10c02e7ab437e3fe5a05e3405115ece5972b2b9f7cd0d68d23c72d5833 1.29MB / 1.29MB                                                                                                        2.0s
=> => extracting sha256:8c7716127147648c1751940b9709b6325f2256290d3201662eca2701cadb2cdf                                                                                                             6.6s
=> => extracting sha256:44350d10c02e7ab437e3fe5a05e3405115ece5972b2b9f7cd0d68d23c72d5833                                                                                                             1.8s
=> => extracting sha256:4dc2c3222cdbf7b5e9d5c68653d42c7289ddf2bfaa17b12c961014755b7d04dd                                                                                                             8.4s
=> => extracting sha256:b25238518c0cca0928b2117b90cee455c3fbdb7d605f92131e5cc92fbfb5b468                                                                                                             0.2s
=> [internal] load build context                                                                                                                                                                   238.8s
=> => transferring context: 530.10MB                                                                                                                                                               238.2s
=> [2/5] WORKDIR /app                                                                                                                                                                                2.4s
=> [3/5] COPY requirements.txt .                                                                                                                                                                     0.4s
=> [4/5] RUN pip install -r requirements.txt                                                                                                                                                        84.0s
=> [5/5] COPY . .                                                                                                                                                                                   42.2s
=> exporting to image                                                                                                                                                                              154.1s
=> => exporting layers                                                                                                                                                                             102.5s
=> => exporting manifest sha256:906868104a01d34b5f7d12faa99899524732aaef0c4901d36b52d7827ef16f45                                                                                                     0.0s
=> => exporting config sha256:0833bb3b056071e09492a5c890c8125a443e7731ae1da2a8ee3117f8e5337862                                                                                                       0.0s
=> => exporting attestation manifest sha256:f1c45f675dad03645cecfc82197df8eca9af4cbae4c5849c70a94138cb6963be                                                                                         0.1s
=> => exporting manifest list sha256:685fad8f53b573bb078a6bc5dd41b0d1968773789c30e0a732654143bc6bfaf4                                                                                                0.1s
=> => naming to [docker.io/library/myapi:latest](http://docker.io/library/myapi:latest)                                                                                                                                                       0.0s
=> => unpacking to [docker.io/library/myapi:latest](http://docker.io/library/myapi:latest)                                                                                                                                                   51.2s
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> docker run -p 8000:8000 myapi
Running experiment...
Numpy version: 2.3.3
Computation: 6

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Invoke-RestMethod "http://localhost:8000/health"

## status

RMD-OK

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Invoke-RestMethod -Method POST -Uri "http://localhost:8000/predict" `

> -ContentType "application/json" `
-Body '{"text":"hello world"}'
> 

## prediction

mystery

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git add src/api.py src/app.py Dockerfile models/ requirements.txt
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git commit -m "Week 6: Added FastAPI + Docker + Streamlit (requirements.txt)"
[main 01f41b0] Week 6: Added FastAPI + Docker + Streamlit (requirements.txt)
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> git push origin main
Enumerating objects: 69, done.
Counting objects: 100% (64/64), done.
Delta compression using up to 8 threads
Compressing objects: 100% (54/54), done.
Writing objects: 100% (54/54), 292.79 KiB | 3.71 MiB/s, done.
Total 54 (delta 25), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (25/25), completed with 5 local objects.
To https://github.com/tcsai/portfolio-25-26-Sy-Lyy.git
a18794a..01f41b0  main -> main




</details>


