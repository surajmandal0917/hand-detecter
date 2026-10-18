# Hand Frame

Hand-tracked AR in the browser. Hold an L shape with one hand and a 3D frame appears with an object inside. Use your other hand to dissolve it into particles and rebuild it as the next object.

## Run
1. Needs internet (loads three.js and MediaPipe from a CDN) and a webcam.
2. In this folder run: `python run.py` (opens http://localhost:8000). Or run `python -m http.server 8000` and open the link yourself.
3. Click Start camera and allow access. Use Chrome or Edge.

## Deploy to Vercel
- Set Vercel's **Root Directory** to this project folder—the one containing `index.html`, `models/`, and `vercel.json`. In this workspace, that is the inner `hand detecter` folder.
- Keep Vercel's **Output Directory** as `.`. The included `vercel.json` sets this so the static deployment serves the app and its `models/` assets from the same folder.
- Redeploy the whole project folder. Do not upload just `index.html`; the `models/` directory and all its subdirectories and files must be included.
- After deployment, check that `https://<your-domain>/models/phoenix/phoenix.fbx` returns successfully. The HUD should report all 5 3D assets loaded; if not, check the browser console and confirm deployed paths preserve filename capitalization.

## Controls
- L shape (thumb + index out, other fingers curled): open the frame
- Other hand open palm: object dissolves into smoke tinted to match its colors
- Other hand fist: colored smoke gathers and rebuilds as the next object
- Space: next object without a second hand. H: show or hide hand skeleton.

## Files
- index.html: the whole project (hand tracking, particle shapes, 3D frame)
- The Tree uses the texture maps in `models/tree/tree/` to build its 3D trunk and canopy.
- To add an object, write a generator like `lily` or `tree` and add it to the `SHAPES` list.
