# Online galleries

- [Key art showcase](https://tqnl.github.io/minecraft-update-artwork/showcase.html): primary sources and preferred added variants.
- [Complete gallery](https://tqnl.github.io/minecraft-update-artwork/index.html): every collected source and added variant.

Both pages are static HTML hosted by GitHub Pages from the root of the `ai-reconstruction` branch. Pushing updates to this branch republishes the site. `.nojekyll` keeps the static files, including the shared `.catalogue` assets, intact.

The showcase selection is recorded in [.catalogue/showcase.json](.catalogue/showcase.json). Source composites and custom title placements appear alongside AI reconstructions, with their actual methods labelled. The separate repaired promotional panorama is available in the complete gallery.

To update the pages after editing the catalogue or selection, run `python tools/render_catalogue.py`, then `python tools/verify_catalogue.py`. Commit and push the generated files. Images remain in their update folders and are shared by both galleries; hosting creates no additional artwork copies.

Both HTML files also work when opened locally. Viewing the hosted galleries needs no repository download, sign-in, or installation.
