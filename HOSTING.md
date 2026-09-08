# GitHub Pages galleries

The `pages-gallery` publication branch combines two static galleries:

- The existing `ai-reconstruction` gallery stays at the site root.
- The `f-quality-review` branch is published under `/f-quality/`.
- `/f-quality/review.html` provides lossless before/after comparisons for all 20 reconstruction outputs.

The two content branches keep their usual update folders and source images. The publication branch contains generated site copies only; it is not the editing branch. Update its two trees from the recorded content commits when publishing another round. GitHub Pages serves `pages-gallery` from `/`, with `.nojekyll`.

Public comparison snapshots under `.catalogue/f-review/before/` intentionally preserve five checkpoint images. All other retained comparisons reuse their unchanged artwork files. Private slides, manual inventory material and local scratch files are excluded.
