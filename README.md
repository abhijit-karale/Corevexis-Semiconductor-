# Corevexis Semiconductor - Website

This repository contains the static website for Corevexis Semiconductor — a cloud-based semiconductor design platform.

Live Site

- Intended GitHub Pages URL: `https://<your-github-username>.github.io/<repo>/`

Local Development

1. Start a simple HTTP server from the project root (recommended):

```powershell
# from project folder
python -m http.server 8000
```

2. Open `http://localhost:8000` in your browser.

Deploy to GitHub Pages

1. Create a new GitHub repository.
2. Initialize local git (already prepared) and add remote:

```bash
git remote add origin git@github.com:USERNAME/REPO.git
git push -u origin main
# or push gh-pages branch if you prefer
git push -u origin gh-pages
```

3. On GitHub: Settings → Pages → select `main` or `gh-pages` branch and Save.

Custom Domain

- To use a custom domain, create a `CNAME` file at the repo root containing your domain (e.g. `example.com`) and push it to GitHub.

Notes

- Assets load from CDN (Font Awesome). No build step required.
- Contact: info@chipnest.com
