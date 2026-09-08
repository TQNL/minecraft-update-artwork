# Reconstruction quality review

All **20 derived images passed at 8/10 or higher after 2 independent critic rounds**, within the three-round limit. **16 files were repaired in place**; the other 4 were retained after review. All 48 source files remain unchanged beside the derivatives.

The reviewers inspected full compositions and native-size details, with extra source comparisons for suspected seams, matte defects and geometry changes. Scores are subjective and do not establish recovery of original high-resolution detail. AI-restored textures and concealed content remain interpretations.

[Open the showcase](https://tqnl.github.io/minecraft-update-artwork/showcase.html) · [Complete gallery](https://tqnl.github.io/minecraft-update-artwork/index.html) · [Recorded prompts](prompts.md) · [Hash-bound results](final.json)

## Scores, newest first

| Asset | Update | Round 1 | Round 2 | Result |
| :--- | :--- | ---: | ---: | :--- |
| [R03](../../artwork/02-chaos-cubed/expanded-composition-rating-removed-2560x1440.png) | Chaos Cubed | 9/10 | 9/10 | Pass |
| [R05](../../artwork/03-tiny-takeover/complete-scene-no-title-2275x1440.png) | Tiny Takeover | 7/10 | 9/10 | Pass |
| [R04](../../artwork/03-tiny-takeover/complete-scene-with-title-2275x1440.png) | Tiny Takeover | 7/10 | 9/10 | Pass |
| [R12](../../artwork/07-spring-to-life/complete-scene-3430x2048.png) | Spring to Life | 8/10 | 8/10 | Pass |
| [R17](../../artwork/10-tricky-trials/expanded-clean-scene-2198x1440.png) | Tricky Trials | 8/10 | 9/10 | Pass |
| [R16](../../artwork/10-tricky-trials/titled-breeze-variant-2196x1235.png) | Tricky Trials | 8/10 | 9/10 | Pass |
| [R21](../../artwork/13-trails-tales/titled-alternate-sniffer-2058x1158.png) | Trails & Tales | 9/10 | 9/10 | Pass |
| [R23](../../artwork/13-trails-tales/promotional-panorama-seams-repaired-4080x1350.png) | Trails & Tales | 8/10 | 9/10 | Pass |
| [R25](../../artwork/14-the-wild-update/titled-landscape-2560x1440.png) | The Wild Update | 8/10 | 8/10 | Pass |
| [R26](../../artwork/14-the-wild-update/square-with-clean-source-centre-2560x2560.png) | The Wild Update | 8/10 | 9/10 | Pass |
| [R28](../../artwork/15-caves-cliffs-part-ii/official-title-composite-2560x1440.png) | Caves & Cliffs Part II | 9/10 | 9/10 | Pass |
| [R30](../../artwork/16-caves-cliffs-part-i/official-title-composite-2560x1440.png) | Caves & Cliffs Part I | 9/10 | 9/10 | Pass |
| [R34](../../artwork/17-nether-update/custom-title-placement-2560x1440.png) | Nether Update | 8/10 | 9/10 | Pass |
| [R37](../../artwork/18-buzzy-bees/larger-alex-variant-2560x1440.png) | Buzzy Bees | 9/10 | 9/10 | Pass |
| [R38](../../artwork/19-village-pillage/clean-scene-with-reference-title-placement-2560x1440.png) | Village & Pillage | 8/10 | 8/10 | Pass |
| [R40A](../../artwork/20-update-aquatic/expanded-banner-no-title-4320x1440.png) | Update Aquatic | 8/10 | 9/10 | Pass |
| [R40B](../../artwork/20-update-aquatic/expanded-banner-with-title-4320x1440.png) | Update Aquatic | 7/10 | 9/10 | Pass |
| [R41](../../artwork/20-update-aquatic/custom-titled-scene-2560x1440.png) | Update Aquatic | 8/10 | 9/10 | Pass |
| [R52](../../artwork/22-exploration-update/trailer-title-reconstruction-6000x3375.png) | Exploration Update | 7/10 | 8/10 | Pass |
| [R49](../../artwork/24-combat-update/combat-enhanced-and-resampled-5120x2880.png) | Combat Update | 8/10 | 8/10 | Pass |

## Repairs

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

## Remaining limits

Some original side regions, PART lettering and terrain retain source softness. AI-restored panoramas, side strips, logos and face crops can contain inferred fine details. Custom title placements remain unofficial. Original source files are available for exact source fidelity.

## Review records

- [Round 1: scores, findings and repair feedback](round-1.json)
- [Round 2: scores, findings and repair feedback](round-2.json)

## Working material excluded

Rejected attempts, baseline backups, crop boards, masks, raw generated outputs and local scripts stay outside the public checkout. They are scratch and review material, can contain local paths, and would duplicate the selected images. Published records include the final files, source lineage, saved prompts, review feedback and hashes. Public images contain no descriptive identity metadata.
