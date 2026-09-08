# F-stage quality review

**20 reconstruction outputs inspected; 5 adjusted; 15 retained; all 48 original source files unchanged.** No new AI generation or shape-restoration masks were used. The changes are restrained edge-contrast adjustments, with a small sharpness-transition adjustment in Aquatic. They cannot recover absent source detail.

[Interactive before/after review](https://tqnl.github.io/minecraft-update-artwork/f-quality/review.html) · [Branch showcase](https://tqnl.github.io/minecraft-update-artwork/f-quality/showcase.html) · [Full gallery](https://tqnl.github.io/minecraft-update-artwork/f-quality/index.html)

## Starting point

The branch checkpoint is `a7397a46086ca22efad503d2033123709fdf7122`. Its untitled Aquatic banner is byte-identical to saved version F, with its P40 outer source regions, P41 centre, sharpening, source joins and earlier small AI water patch. The titled banner uses that same scene with the existing custom title overlay. The later G/H coral masks and AI water field are not the basis for these two banners.

F was a saved Aquatic intermediate, not a complete repository snapshot. The other 18 outputs retain the finished source-restoration state at `4be74cbf6b084b4d63032de8751057a73e250805`, including its completed seam fixes. The checkpoint commit is preserved, so this round can be compared or reverted cleanly.

## Review and limitations

Each full composition and four native detail crops was inspected. Changed candidates were compared at native size against the checkpoint for halos, loss of detail, hard adjustment boundaries and title changes. This is a visual inspection by the implementing assistant, not a new independent critic score. Prior three-round scores belong to their historical image hashes and are not presented as approval of these changes. Final preference is open for user review.

Aquatic's source-specific bubble designs and sharpness levels still differ. Its source reefs remain soft, and the old small title-removal water fill is inherited. The light sharpening and transition smoothing preserve positions and silhouettes; they do not reconstruct or redraw bubbles. Combat was retained because further sharpening would exaggerate the limits of its 1280 x 720 source.

## Decisions, newest first

| Asset | Update | Decision |
| :--- | :--- | :--- |
| [R03](../artwork/02-chaos-cubed/expanded-composition-rating-removed-2560x1440.png) | Chaos Cubed | Retained: repaired wall, lettering-free scene and block edges are already crisp; extra sharpening would add halos. |
| [R05](../artwork/03-tiny-takeover/complete-scene-no-title-2275x1440.png) | Tiny Takeover | Retained: clean petal and sky joins, sharp native centre; no useful additional sharpening. |
| [R04](../artwork/03-tiny-takeover/complete-scene-with-title-2275x1440.png) | Tiny Takeover | Retained: same clean scene as R05, with readable title edges; no useful additional sharpening. |
| [R12](../artwork/07-spring-to-life/complete-scene-3430x2048.png) | Spring to Life | Retained: birch joins and corner fills are coherent; existing edge outlines would become stronger with sharpening. |
| [R17](../artwork/10-tricky-trials/expanded-clean-scene-2198x1440.png) | Tricky Trials | Adjusted: restrained luminance sharpening only in the softer outer source strips, feathered into the native centre. |
| [R16](../artwork/10-tricky-trials/titled-breeze-variant-2196x1235.png) | Tricky Trials | Adjusted: restrained luminance sharpening in the outer source strips and restored Breeze region, with soft adjustment boundaries. |
| [R21](../artwork/13-trails-tales/titled-alternate-sniffer-2058x1158.png) | Trails & Tales | Retained: title and scene edges are already clear; further sharpening offers little benefit. |
| [R23](../artwork/13-trails-tales/promotional-panorama-seams-repaired-4080x1350.png) | Trails & Tales | Adjusted: mild luminance sharpening with a noise threshold across the soft source panorama; preserved its repaired separator and existing haze. |
| [R25](../artwork/14-the-wild-update/titled-landscape-2560x1440.png) | The Wild Update | Retained: scene and title are sufficiently sharp; extra edge contrast would exaggerate outlines. |
| [R26](../artwork/14-the-wild-update/square-with-clean-source-centre-2560x2560.png) | The Wild Update | Retained: square composition transitions and block surfaces are coherent; no additional adjustment needed. |
| [R28](../artwork/15-caves-cliffs-part-ii/official-title-composite-2560x1440.png) | Caves & Cliffs Part II | Retained: scene and main title are crisp; soft Part II lettering cannot gain actual detail from more sharpening. |
| [R30](../artwork/16-caves-cliffs-part-i/official-title-composite-2560x1440.png) | Caves & Cliffs Part I | Retained: scene and main title are crisp; extra sharpening of the small Part I label risks ringing. |
| [R34](../artwork/17-nether-update/custom-title-placement-2560x1440.png) | Nether Update | Retained: title and reconstructed background transitions remain clean at native size. |
| [R37](../artwork/18-buzzy-bees/larger-alex-variant-2560x1440.png) | Buzzy Bees | Retained: character replacement and adjoining blocks remain coherent and sharp. |
| [R38](../artwork/19-village-pillage/clean-scene-with-reference-title-placement-2560x1440.png) | Village & Pillage | Retained: clean custom title matte and strong source edges; extra sharpening is unnecessary. |
| [R40A](../artwork/20-update-aquatic/expanded-banner-no-title-4320x1440.png) | Update Aquatic | Adjusted from exact F: modest luminance sharpening in enlarged side regions and gently feathered, subpixel-radius smoothing around the two source sharpness transitions. Bubble positions and coral geometry are retained. |
| [R40B](../artwork/20-update-aquatic/expanded-banner-with-title-4320x1440.png) | Update Aquatic | Adjusted from F scene with the existing title: same scene changes as R40A; title overlay pixels retained exactly. |
| [R41](../artwork/20-update-aquatic/custom-titled-scene-2560x1440.png) | Update Aquatic | Retained: native Aquatic scene and custom title remain sharp; this is the separate 16:9 variant, not the F banner. |
| [R52](../artwork/22-exploration-update/trailer-title-reconstruction-6000x3375.png) | Exploration Update | Retained: block silhouettes and title edges are already crisp; additional contrast would strengthen fine edge ringing. |
| [R49](../artwork/24-combat-update/combat-enhanced-and-resampled-5120x2880.png) | Combat Update | Retained: already sharpened 4x source resampling; more sharpening would amplify source stair steps and compression rather than recover detail. |

## Processing and public files

The [processing code](../tools/quality_adjustments.py) contains the exact parameters. Sharpening operates on luminance, rejects very small variations, caps contrast changes and limits new local overshoot. It uses no warping, generated textures, selective coral replacement, global saturation change or added resolution. Aquatic additionally mixes a small amount of a 0.65-pixel Gaussian smoothing around its two source transitions, feathered over a wider band. Titled/untitled Aquatic scene pixels are shared, and title-overlay pixels are preserved exactly.

The [machine-readable report](quality-review/final.json) records baseline/final hashes, per-image decisions and measured pixel changes. Five lossless checkpoint PNGs under `.catalogue/f-review/before/` support the live comparisons; these are intentional public review assets. Unchanged images reuse their normal artwork files. Final derivatives remain alongside originals in the usual update folders.

Private slides, manual inventory work, scratch masks, discarded trials, local paths, temporary inspection boards and logs remain excluded. The public branch includes final artwork, these five review baselines, reproducible processing code and concise review records. No personal author or image metadata is added.
