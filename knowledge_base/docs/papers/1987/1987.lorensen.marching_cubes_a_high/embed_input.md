<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Marching Cubes: A High Resolution 3D Surface Construction Algorithm

Topics include Marching cubes, Isosurface extraction, Volume visualization, Medical imaging, Computer graphics, Surface reconstruction, 3D visualization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Lorensen and Cline introduce Marching Cubes, a table-driven algorithm for extracting polygonal isosurfaces from volumetric scalar data. The paper became foundational in scientific visualization and medical imaging because it made high-resolution 3D surface construction practical from sampled volumes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a new algorithm, called marching cubes, that creates triangle models of constant density surfaces from 3D medical data. Using a divide-and-conquer approach to generate inter-slice connectivity, we create a case table that defines triangle topology. The algorithm processes the 3D medical data in scan-line order and calculates triangle vertices using linear interpolation. We find the gradient of the original data, normalize it, and use it as a basis for shading the models. The detail in images produced from the generated surface models is the result of maintaining the inter-slice connectivity, surface data, and gradient information present in the original 3D data. Results from computed tomography (CT), magnetic resonance (MR), and single-photon emission computed tomography (SPECT) illustrate the quality and functionality of marching cubes. We also discuss improvements that decrease processing time and add solid modeling capabilities.
