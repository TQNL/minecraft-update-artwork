# Reconstruction results

All 24 update families through Combat Update (1.9) have been assessed. The branch contains 20 derived images alongside 48 preserved source assets. The two older standalone title families remain in the source collection.

Completion records the requested variants and review decisions. Resampling cannot recover original detail, and synthesized hidden content remains an interpretation. The latest quality pass repairs resolution transitions, soft detail crops and title mattes. Fine restored details remain inferred; some source softness remains. See the [20-image quality review](quality-review/README.md) for all scores and repairs.

All image variants live together in their update folder under `artwork/`. Each folder with additions includes a short README; detailed validation remains here.

## Results, newest first

| Update | Delivered variants | Quality limits |
| :--- | :--- | :--- |
| Wilderness Bound | Sources retained; no derivative requested | No additional reconstruction limitation. |
| Chaos Cubed | [R03](../artwork/02-chaos-cubed/expanded-composition-rating-removed-2560x1440.png) (2560 x 1440) | The wall behind the ratings badge is synthesized; no uncovered original is available. |
| Tiny Takeover | [R05](../artwork/03-tiny-takeover/complete-scene-no-title-2275x1440.png) (2275 x 1440); [R04](../artwork/03-tiny-takeover/complete-scene-with-title-2275x1440.png) (2275 x 1440) | Corner content is synthesized. Added sides retain the detail limit of the smaller JPEG source. |
| Mounts of Mayhem | Sources retained; no derivative requested | No additional reconstruction limitation. |
| The Copper Age | Sources retained; no derivative requested | No additional reconstruction limitation. |
| Chase the Skies | Sources retained; no derivative requested | No additional reconstruction limitation. |
| Spring to Life | [R12](../artwork/07-spring-to-life/complete-scene-3430x2048.png) (3430 x 2048) | Missing corners are synthesized. Landscape sides retain their source compression and are resampled to the square image scale. |
| The Garden Awakens | Sources retained; no derivative requested | No additional reconstruction limitation. |
| Bundles of Bravery | Sources retained; no derivative requested | No additional reconstruction limitation. |
| Tricky Trials | [R17](../artwork/10-tricky-trials/expanded-clean-scene-2198x1440.png) (2198 x 1440); [R16](../artwork/10-tricky-trials/titled-breeze-variant-2196x1235.png) (2196 x 1235) | Corner masonry and restored side-strip textures are inferred. Original P16 lettering retains its source detail; the enhanced foreground Breeze contains synthesized detail. |
| Armored Paws | Sources retained; no derivative requested | Only a 1170 x 500 banner source is available. |
| Bats and Pots | Sources retained; no derivative requested | Only a 1170 x 500 banner source is available. |
| Trails & Tales | [R21](../artwork/13-trails-tales/titled-alternate-sniffer-2058x1158.png) (2058 x 1158); [R23](../artwork/13-trails-tales/promotional-panorama-seams-repaired-4080x1350.png) (4080 x 1350) | R21 retains the original P21 title and alternate Sniffer detail. R23 uses overlapping AI restoration; fine textures are inferred and may look processed at native size. |
| The Wild Update | [R25](../artwork/14-the-wild-update/titled-landscape-2560x1440.png) (2560 x 1440); [R26](../artwork/14-the-wild-update/square-with-clean-source-centre-2560x2560.png) (2560 x 2560) | The square gains P24 detail in its shared 56 percent; P26-only regions retain their original detail limit. P25 title pixels retain the original 1920-pixel-wide source detail. |
| Caves & Cliffs Part II | [R28](../artwork/15-caves-cliffs-part-ii/official-title-composite-2560x1440.png) (2560 x 1440) | Main logo uses the larger official P32 source; PART II retains P28 detail. |
| Caves & Cliffs Part I | [R30](../artwork/16-caves-cliffs-part-i/official-title-composite-2560x1440.png) (2560 x 1440) | Main logo uses the larger official P32 source; PART I retains P30 detail. |
| Nether Update | [R34](../artwork/17-nether-update/custom-title-placement-2560x1440.png) (2560 x 1440) | Custom title placement is unofficial. Fine lettering texture is inferred by local AI restoration of the small original logo. |
| Buzzy Bees | [R37](../artwork/18-buzzy-bees/larger-alex-variant-2560x1440.png) (2560 x 1440) | Alex enhancement contains synthesized edge and surface detail. |
| Village & Pillage | [R38](../artwork/19-village-pillage/clean-scene-with-reference-title-placement-2560x1440.png) (2560 x 1440) | Derived composition combines official scene and lettering; this exact combination is not an original official release. |
| Update Aquatic | [R40A](../artwork/20-update-aquatic/expanded-banner-no-title-4320x1440.png) (4320 x 1440); [R40B](../artwork/20-update-aquatic/expanded-banner-with-title-4320x1440.png) (4320 x 1440); [R41](../artwork/20-update-aquatic/custom-titled-scene-2560x1440.png) (2560 x 1440) | Outer reefs, water and fine bubble details are locally AI-restored interpretations. Title placements are custom and unofficial; restored logo texture is inferred. |
| World of Color Update | Sources retained; no derivative requested | No additional reconstruction limitation. |
| Exploration Update | [R52](../artwork/22-exploration-update/trailer-title-reconstruction-6000x3375.png) (6000 x 3375) | The title is an AI reconstruction of the small trailer reference, not the original high-resolution logo; fine cracks and shading are inferred. The wall behind the relocated Vex is locally reconstructed; fine concealed geometry cannot be confirmed from the sources. |
| Frostburn Update | Sources retained; no derivative requested | Only a 1280 x 720 scene is collected; the separate fan title does not supply additional scene detail. |
| Combat Update | [R49](../artwork/24-combat-update/combat-enhanced-and-resampled-5120x2880.png) (5120 x 2880) | This is an AI-enhanced and resampled derivative, not native 5K source artwork. The initial generation was 1672 x 941, followed by separate detail-crop restorations and resampling. Fine scene, facial and lettering detail is inferred; the original remains available for strict source fidelity. |

## What is excluded and why

- P27 and P33 were removed from the current collection as superseded title treatments. P44 and P46 were replaced by the official 16:9 Exploration trailer reference S52. Their stable PDF IDs remain in the mapping so the review instructions still make sense.
- Presentations, private inventories, local exports, logs, environment files and OS-generated files are excluded by `.gitignore`; they are working material rather than archive artwork and can contain local identity or edit history.
- Scratch masks, rejected generations, comparison crops and local orchestration notes are not published. Selected outputs, generation prompts, source lineage and validation are published.
- Source image metadata and local personal paths are excluded. Creator attribution is retained. The repository owner remains visible through GitHub.

The only ignored files currently inside this checkout are Python bytecode caches created by validation. Other excluded working material lives outside the checkout. Git history was not rewritten as part of these collection removals.

## Verification

See the [audit report](final-audit.json), [per-update progress](progress.json), and [generation prompts](prompts). Run `python tools/verify_catalogue.py` for asset integrity, or `python tools/audit_reconstruction.py` for the full branch audit (requires Git, Pillow and remote access).
