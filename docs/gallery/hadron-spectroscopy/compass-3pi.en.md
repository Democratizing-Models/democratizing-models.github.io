---
analysis_profile:
  category: measure
  field: "Hadron spectroscopy"
  reason: "Unnormalized, acceptance corrected partial-wave amplitudes and intensities; phase-space integration supplies the normalization."
  note: "Approximate analysis-scale values."
  metrics:
    forward_model_core_hours: 0.1
    parameter_count: 1000 (resonance model fit) + 100000 (partial wave decomposition)
    analysis_core_hours: 1000
    data_input_mb: 1000
    external_frameworks: 2
    software_stack_lines: 1000000
    citation_count: 100
---

# COMPASS · $\pi p\to3\pi p$ partial waves

Public complex amplitudes and covariance matrices provide inputs for a reduced resonance-model reconstruction of $\pi p\to3\pi p$.

!!! info "Reproduction status"

    **Scoped**. Independent validation pending. Status updated 2026-07-17.

## Scientific model

This case concerns closed-form amplitude. Resonance-model curves on published wave intensities and phases for a reduced wave subset

The reproduction objective below defines the current scope; a complete published-analysis reproduction is not asserted.

## Model ingredients

Reusing this model requires the ingredients below. Availability and limitations
are described in the reproduction evidence.

- Beam and target process
- mass and momentum-transfer bins
- partial waves, reflectivity and spin conventions
- isobar parameterizations and rank assumptions
- acceptance corrections, spin-density matrices and systematic wave-set variations.

## Reproduction objective and evidence

**Objective:** Resonance-model curves on published wave intensities and phases for a reduced wave subset

**Scope and limitations:** The reduced forward-model reproduction is still to be built.

## Figures

![COMPASS · Partial-wave analysis: reference objective figure](../../assets/gallery/compass-3pi/target_1pp_wave_intensities.png)

*Reference figure from the publication cited below, showing an example of the $1^{++}$ partial wave.*

## HEPdata

- Transition Amplitudes · [DOI: 10.17182/hepdata.82958.v1/t1](https://doi.org/10.17182/hepdata.82958.v1/t1)
- Decay Phase-Space Volume of Partial Waves · [DOI: 10.17182/hepdata.82958.v1/t2](https://doi.org/10.17182/hepdata.82958.v1/t2)

## Publications

- **COMPASS:2018uzl** (2018) · [DOI: 10.1103/PhysRevD.98.092003](https://doi.org/10.1103/PhysRevD.98.092003) · [arXiv:1802.05913](https://arxiv.org/abs/1802.05913)


[Back to model gallery](../index.md)
