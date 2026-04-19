# How to Upload Your Project to GitHub

## Step 1 — Create a GitHub account (if you don't have one)
Go to https://github.com and sign up for a free account.

## Step 2 — Create a new repository
1. Once logged in, click the **+** button in the top-right corner → **New repository**
2. Give it a name, e.g. `note-visualiser`
3. Set it to **Public** (so others can see it) or **Private** (just for you)
4. **Do NOT** tick "Add a README file" — you already have one
5. Click **Create repository**

## Step 3 — Prepare your project folder
Copy the three files I created into your project folder:

```
COMP112_FINAL_VV/NOTE_VISUALISER_CODE_AND_CONTENTS/
├── COMP112_final_VV.py      ← already here
├── pyaudio.py               ← already here
├── A.wav, B.wav, ... Gs.wav ← already here
├── README.md                ← copy this in   ✅
├── .gitignore               ← copy this in   ✅
└── requirements.txt         ← copy this in   ✅
```

> Note: `.gitignore` starts with a dot — it may be hidden on your Mac.
> In Finder, press **Cmd + Shift + .** to show hidden files.

## Step 4 — Open Terminal
Press **Cmd + Space**, type **Terminal**, and press Enter.

## Step 5 — Navigate to your project folder
In Terminal, type (adjust the path to match where your folder actually lives):

```bash
cd ~/Desktop/Portfolio/IDEAS/COMP112_FINAL_VV/NOTE_VISUALISER_CODE_AND_CONTENTS
```

## Step 6 — Set up Git and push to GitHub

Run these commands one at a time:

```bash
# Initialise git in the folder
git init

# Add all your files
git add .

# Make your first commit
git commit -m "Initial commit — COMP112 Note Visualiser project"

# Connect to your GitHub repo (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/note-visualiser.git

# Push everything to GitHub
git branch -M main
git push -u origin main
```

When prompted, enter your GitHub username and password.
> **Tip:** GitHub may ask you to use a Personal Access Token instead of your password.
> You can create one at: GitHub → Settings → Developer settings → Personal access tokens → Generate new token.
> Give it the **repo** scope and use it in place of your password.

## Step 7 — Check your repo
Go to `https://github.com/YOUR_USERNAME/note-visualiser` — your project should be live! 🎉

---

## What each file does

| File | Purpose |
|------|---------|
| `README.md` | Describes your project on the GitHub page — the first thing visitors see |
| `.gitignore` | Tells Git which files to ignore (e.g. `.DS_Store`, output `.eps` files) |
| `requirements.txt` | Lists Python packages someone needs to install to run your project |
