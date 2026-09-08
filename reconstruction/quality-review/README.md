> Historical report for the previous reconstruction branch. See [F-stage branch review](../F-QUALITY.md) for this branch. Prior scores do not apply to changed files.

# Reconstruction quality review

At the end of the previous branch, all **20 derivatives passed at 8/10 or higher after three independent critic rounds**. Those scores refer to the recorded historical hashes. The latest round includes a source-geometry correction prompted by AI changes to the Minecraft voxel style. Nine files were corrected in this revision, following the earlier 16-image quality pass. All 48 originals remain unchanged beside the derivatives.

[Source geometry comparisons and corrections](source-geometry.md) · [Historical round-3 hashes](after-round-3.json) · [Earlier generation prompts](prompts.md)

The scores are subjective visual assessments. Original low-resolution regions can remain soft, and retained hidden-corner, water or logo reconstruction is not verified original detail.

## Scores, newest first

| Asset | Update | Round 1 | Round 2 | Round 3 | Result |
| :--- | :--- | ---: | ---: | ---: | :--- |
| [R03](../../artwork/02-chaos-cubed/expanded-composition-rating-removed-2560x1440.png) | Chaos Cubed | 9/10 | 9/10 | 9/10 | Pass |
| [R05](../../artwork/03-tiny-takeover/complete-scene-no-title-2275x1440.png) | Tiny Takeover | 7/10 | 9/10 | 8.8/10 | Pass |
| [R04](../../artwork/03-tiny-takeover/complete-scene-with-title-2275x1440.png) | Tiny Takeover | 7/10 | 9/10 | 8.8/10 | Pass |
| [R12](../../artwork/07-spring-to-life/complete-scene-3430x2048.png) | Spring to Life | 8/10 | 8/10 | 8.7/10 | Pass |
| [R17](../../artwork/10-tricky-trials/expanded-clean-scene-2198x1440.png) | Tricky Trials | 8/10 | 9/10 | 8.6/10 | Pass |
| [R16](../../artwork/10-tricky-trials/titled-breeze-variant-2196x1235.png) | Tricky Trials | 8/10 | 9/10 | 8.4/10 | Pass |
| [R21](../../artwork/13-trails-tales/titled-alternate-sniffer-2058x1158.png) | Trails & Tales | 9/10 | 9/10 | 9.2/10 | Pass |
| [R23](../../artwork/13-trails-tales/promotional-panorama-seams-repaired-4080x1350.png) | Trails & Tales | 8/10 | 9/10 | 8.5/10 | Pass |
| [R25](../../artwork/14-the-wild-update/titled-landscape-2560x1440.png) | The Wild Update | 8/10 | 8/10 | 9.1/10 | Pass |
| [R26](../../artwork/14-the-wild-update/square-with-clean-source-centre-2560x2560.png) | The Wild Update | 8/10 | 9/10 | 9.1/10 | Pass |
| [R28](../../artwork/15-caves-cliffs-part-ii/official-title-composite-2560x1440.png) | Caves & Cliffs Part II | 9/10 | 9/10 | 9/10 | Pass |
| [R30](../../artwork/16-caves-cliffs-part-i/official-title-composite-2560x1440.png) | Caves & Cliffs Part I | 9/10 | 9/10 | 9/10 | Pass |
| [R34](../../artwork/17-nether-update/custom-title-placement-2560x1440.png) | Nether Update | 8/10 | 9/10 | 8.6/10 | Pass |
| [R37](../../artwork/18-buzzy-bees/larger-alex-variant-2560x1440.png) | Buzzy Bees | 9/10 | 9/10 | 8.8/10 | Pass |
| [R38](../../artwork/19-village-pillage/clean-scene-with-reference-title-placement-2560x1440.png) | Village & Pillage | 8/10 | 8/10 | 9.1/10 | Pass |
| [R40A](../../artwork/20-update-aquatic/expanded-banner-no-title-4320x1440.png) | Update Aquatic | 8/10 | 9/10 | 8.1/10 | Pass |
| [R40B](../../artwork/20-update-aquatic/expanded-banner-with-title-4320x1440.png) | Update Aquatic | 7/10 | 9/10 | 8.1/10 | Pass |
| [R41](../../artwork/20-update-aquatic/custom-titled-scene-2560x1440.png) | Update Aquatic | 8/10 | 9/10 | 8.7/10 | Pass |
| [R52](../../artwork/22-exploration-update/trailer-title-reconstruction-6000x3375.png) | Exploration Update | 7/10 | 8/10 | 8.5/10 | Pass |
| [R49](../../artwork/24-combat-update/combat-enhanced-and-resampled-5120x2880.png) | Combat Update | 8/10 | 8/10 | 8.8/10 | Pass |

## Latest corrections

- **R05:** Removed sampling-boundary streaks using the clean earlier petal/sky pixels; retained source shapes and existing corner fills.
- **R04:** Removed sampling-boundary streaks using the clean earlier petal/sky pixels; retained source shapes and existing corner fills.
- **R12:** Removed sampling-boundary streaks from the source blend, including the upper-left birch trunk; retained existing block geometry and corner fills.
- **R17:** Restored registered P16 side geometry and P17 centre from the source composite; retained only the pre-existing unsourced corner fills.
- **R16:** Restored source side strips and the original P16 Breeze-region masonry, wind and character shapes using a registered source crop with an 18-pixel edge blend.
- **R23:** Restored original P23 geometry and textures with bounded source sharpening. Retained only a 66-pixel-wide strip of the earlier AI result at the damaged separator, blended through gradient-domain compositing to remove the tonal stripe without affecting adjacent source silhouettes.
- **R40A:** Restored registered original coral, kelp and sand surfaces through a solid-region mask, retaining coherent restored water/bubbles to avoid reintroducing the conflicting source backgrounds. Fine water detail remains inferred.
- **R40B:** Shared source-restored coral, kelp and sand geometry from R40A; retained its reviewed water/bubble field and custom title matte.
- **R49:** Rebuilt from P49 using bounded source sharpening and Lanczos resampling only. Restored original terrain, wings, swords, character and title geometry; no generated scene detail remains.

## Earlier repairs (rounds 1-2)

These describe earlier stages. The source-geometry correction above supersedes broad AI restoration where specified. Earlier hashes remain in [the round-2 snapshot](after-round-2.json).

- **R05:** Source transition softened over 110 pixels instead of an abrupt hard join; original scene retained. Removed warped-source boundary streak with clean baseline petal pixels inside x80-215, y1328-1363; 8-pixel feather.
- **R04:** Source transition softened over 110 pixels instead of an abrupt hard join; original scene retained. Removed warped-source boundary streak with clean baseline petal pixels inside x80-215, y1328-1363; 8-pixel feather.
- **R12:** Source transition softened over 110 pixels instead of an abrupt hard join; original scene retained.
- **R17:** Localized AI restoration: tricky-left Localized AI restoration: tricky-right
- **R16:** Transferred matching restored side strips from clean R17; title/Breeze preserved.
- **R23:** Three registered overlapping AI-restored tiles with broad original color retained.
- **R25:** Reblended the low/high-resolution horizontal joins over a 150-pixel transition, retaining unique source content.
- **R26:** Reblended the low/high-resolution horizontal joins over a 150-pixel transition, retaining unique source content.
- **R28:** Larger original P32 title pixels replace the smaller title source; part lettering retained.
- **R30:** Larger original P32 title pixels replace the smaller title source; part lettering retained.
- **R34:** Localized AI restoration: nether-title
- **R40A:** Localized AI restoration: aquatic-left Localized AI restoration: aquatic-right
- **R40B:** Shared restored banner scene and sharpened original-style title treatment. Removed carried blue-background halo using the title dark silhouette as matte and clean R40A scene beneath.
- **R41:** Localized AI restoration: aquatic-title
- **R52:** Repaired transparent pinholes and broken edges in reconstructed title matte. Reopened the C aperture at x4716-4828, y350-399 using the registered original scene; preserved surrounding black logo extrusion.
- **R49:** Localized AI restoration: combat-alex Localized AI restoration: combat-steve Localized AI restoration: combat-title

## Review records

- [Round 1](round-1.json)
- [Round 2](round-2.json)
- [Round 3](round-3.json)

## Working material excluded

Scratch generations, masks, crop boards, rejected attempts, local backups and orchestration scripts remain outside the public checkout. They duplicate working material and can include personal paths. Final artwork, source lineage, prompts, source-comparison findings and review hashes are published.
