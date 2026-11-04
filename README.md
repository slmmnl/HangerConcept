# Flat triangle hanger: interactive CAD

Static site (no build step). Open `index.html` through any web server, or host it on GitHub Pages.

## Publish on GitHub Pages
1. Create a new public repository, for example `hanger-cad`.
2. Upload everything in this folder to the repository root (`index.html`, `js/`, `models/`, `.nojekyll`).
3. Repository Settings > Pages > Build and deployment > Source: Deploy from a branch, branch `main`, folder `/ (root)`.
4. After a minute the site is live at `https://<username>.github.io/<repo>/`.
5. Make the QR code: `python3 make_qr.py https://<username>.github.io/<repo>/ qr.png` (needs `pip install qrcode[pil]`).

## Local test
`python3 -m http.server 8000` then open http://localhost:8000
(opening index.html by double-click will not work: browsers block loading the model files from file://).

Concept CAD. All ratings and sizes are estimates; nothing here has been built or tested.
