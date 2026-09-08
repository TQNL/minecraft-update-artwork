# Source geometry correction

The earlier AI restoration changed some source block textures, silhouettes and surface details. This revision checks all 20 derivatives against available source regions and corrects nine files. No new images were generated for this correction.

Coral, kelp and sand in both Aquatic banners now use registered original surfaces. Their coherent restored water and bubbles remain in place so the different source backgrounds do not form a hard join. Tricky Trials sides/Breeze, the Trails panorama and Combat use source-backed shapes. Tiny Takeover and Spring to Life also lose remaining sampling-boundary streaks; the panorama separator retains only a narrow, gradient-blended strip of the earlier AI repair.

Source-backed repairs can be softer than generated detail. Hidden corner/wall content and retained AI water or logo detail cannot be verified as exact original pixels. All 48 original files remain unchanged.

## Source comparisons, newest first

### [R03: Chaos Cubed](../../artwork/02-chaos-cubed/expanded-composition-rating-removed-2560x1440.png)

Covered rating wall checked against adjacent P03 wall pattern and P02 composition. Pixel steps and flat block surfaces remain coherent. Hidden exact pixels cannot be verified.

### [R05: Tiny Takeover](../../artwork/03-tiny-takeover/complete-scene-no-title-2275x1440.png)

P04/P05 registered source coverage and inferred corner joins checked. Sampling-boundary line corrected; unsourced corner shapes remain an interpretation.

Correction: Removed sampling-boundary streaks using the clean earlier petal/sky pixels; retained source shapes and existing corner fills.

### [R04: Tiny Takeover](../../artwork/03-tiny-takeover/complete-scene-with-title-2275x1440.png)

P04/P05 registered source coverage and inferred corner joins checked. Sampling-boundary line corrected; unsourced corner shapes remain an interpretation.

Correction: Removed sampling-boundary streaks using the clean earlier petal/sky pixels; retained source shapes and existing corner fills.

### [R12: Spring to Life](../../artwork/07-spring-to-life/complete-scene-3430x2048.png)

P11/P12 source/composite and all four missing corners checked. Synthesized blocks follow adjoining straight faces; no additional deformation found. Exact missing corner content is unavailable. Critic native inspection found an upper birch sampling streak; it was removed using clean existing source-composite pixels.

Correction: Removed sampling-boundary streaks from the source blend, including the upper-left birch trunk; retained existing block geometry and corner fills.

### [R17: Tricky Trials](../../artwork/10-tricky-trials/expanded-clean-scene-2198x1440.png)

P16 side strips compared to generated restoration: repeated masonry and edge patterns had shifted. Restored earlier source composite.

Correction: Restored registered P16 side geometry and P17 centre from the source composite; retained only the pre-existing unsourced corner fills.

### [R16: Tricky Trials](../../artwork/10-tricky-trials/titled-breeze-variant-2196x1235.png)

P16 side strips and full alternate Breeze crop compared. Replaced regenerated masonry/wind shapes with registered source pixels.

Correction: Restored source side strips and the original P16 Breeze-region masonry, wind and character shapes using a registered source crop with an 18-pixel edge blend.

### [R21: Trails & Tales](../../artwork/13-trails-tales/titled-alternate-sniffer-2058x1158.png)

Direct P21/P22 source composite; no generated geometry. Retained.

### [R23: Trails & Tales](../../artwork/13-trails-tales/promotional-panorama-seams-repaired-4080x1350.png)

P23 compared across camel ground, distant trees and Sniffer. Broad AI surface changes were replaced with source geometry. The damaged separator retains a 66-pixel-wide strip from the earlier AI result after gradient-domain blending; exact hidden separator detail remains inferred.

Correction: Restored original P23 geometry and textures with bounded source sharpening. Retained only a 66-pixel-wide strip of the earlier AI result at the damaged separator, blended through gradient-domain compositing to remove the tonal stripe without affecting adjacent source silhouettes.

### [R25: The Wild Update](../../artwork/14-the-wild-update/titled-landscape-2560x1440.png)

Direct P24/P25 aligned source composite; no generated geometry. Retained.

### [R26: The Wild Update](../../artwork/14-the-wild-update/square-with-clean-source-centre-2560x2560.png)

Direct P24/P26 source composite; no generated geometry. Retained.

### [R28: Caves & Cliffs Part II](../../artwork/15-caves-cliffs-part-ii/official-title-composite-2560x1440.png)

Official P32 logo, P28 part lettering and P29 scene; no generated geometry. Retained.

### [R30: Caves & Cliffs Part I](../../artwork/16-caves-cliffs-part-i/official-title-composite-2560x1440.png)

Official P32 logo, P30 part lettering and P31 scene; no generated geometry. Retained.

### [R34: Nether Update](../../artwork/17-nether-update/custom-title-placement-2560x1440.png)

Full AI-restored logo compared with original P35 treatment. Letter contours remain coherent; fine cracks are inferred. Retained.

### [R37: Buzzy Bees](../../artwork/18-buzzy-bees/larger-alex-variant-2560x1440.png)

Larger Alex compared directly with P37 crop: body silhouette, square facial pixels, hand, bottle and leg shapes remain coherent. Retained.

### [R38: Village & Pillage](../../artwork/19-village-pillage/clean-scene-with-reference-title-placement-2560x1440.png)

Source P38/P39 lettering/scene composite; no generated geometry. Retained.

### [R40A: Update Aquatic](../../artwork/20-update-aquatic/expanded-banner-no-title-4320x1440.png)

P40 registered outer reefs compared with AI crop: coral textures, kelp edges and sand details had changed. Original solid geometry restored selectively; inferred water/bubbles retained to avoid conflicting source backgrounds.

Correction: Restored registered original coral, kelp and sand surfaces through a solid-region mask, retaining coherent restored water/bubbles to avoid reintroducing the conflicting source backgrounds. Fine water detail remains inferred.

### [R40B: Update Aquatic](../../artwork/20-update-aquatic/expanded-banner-with-title-4320x1440.png)

Same reef correction as R40A. Title compared to P40 reference and existing clean matte retained.

Correction: Shared source-restored coral, kelp and sand geometry from R40A; retained its reviewed water/bubble field and custom title matte.

### [R41: Update Aquatic](../../artwork/20-update-aquatic/custom-titled-scene-2560x1440.png)

Full restored title compared with original P40 logo treatment; overall letter contours remain coherent. Scene is P41 outside title crop. Retained.

### [R52: Exploration Update](../../artwork/22-exploration-update/trailer-title-reconstruction-6000x3375.png)

Trailer S52 and original P45 scene checked: source Vex remains cubic and local wall fill has straight planar edges. Exact hidden wall and fine logo details cannot be verified.

### [R49: Combat Update](../../artwork/24-combat-update/combat-enhanced-and-resampled-5120x2880.png)

P49 source compared at terrain, roofs, wings, faces and title. AI added bevels and changed small shapes across the scene. Rebuilt through non-generative sharpening/resampling from P49.

Correction: Rebuilt from P49 using bounded source sharpening and Lanczos resampling only. Restored original terrain, wings, swords, character and title geometry; no generated scene detail remains.

[Final independent review](round-3.json) · [All review scores](README.md) · [Current file hashes](final.json)
